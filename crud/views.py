from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from crud.forms import TaskForm, User_registration_Form
from crud.models import Taks
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password,make_password


# Create your views here.


def principal (request):
    return render(request, "principal.html")


@login_required
def navegacion (request):
    return render (request,"navegacion.html")


def signup (request):
    
    if request.method == "GET":
        print("procesando datos")
        return render (request, "signup.html", {
        "form": User_registration_Form
    })
        
    else:
       
        if request.POST["password_1"] == request.POST ["password_2"]:
            print(request.POST)
            print("Analizando datos de usuario")
            
            email = request.POST["email"].lower()
                       
            if User.objects.filter(email = email).exists():
                return render (request, "signup.html", {
                    "form": User_registration_Form,
                    "respuesta": "Correo ya registrado"
                    })
                
            else:
                
                first_name = request.POST["first_name"]
                
                if User.objects.filter(first_name = first_name).exists():
                    return render (request,"signup.html", {
                        "form": User_registration_Form,
                        "respuesta": "Nombre de usuario ya registrado"
                    })
                
                else:
                    key = request.POST["password_1"]
                    
                    if len(key) <= 7:
                        return render (request,"signup.html", {
                            "form": User_registration_Form,
                            "respuesta": "Contraseña mínima: 8 caracteres"
                        })
                    
                    else:  
                        try:
                            user = User.objects.create_user(username = request.POST["username"],first_name = request.POST["first_name"].capitalize(), last_name = request.POST["last_name"].capitalize(), email = request.POST["email"], password = request.POST["password_1"])
                            user.save()
                            login(request,user)
                            return redirect ("/new_task/")
                
        
                        except:
                            return render (request, "signup.html", {
                            "form": User_registration_Form,
                            "respuesta": "El nombre de usuario ya existe Intenta con otro"
                            })
                                                   
        else:
            return render (request, "signup.html", {
            "form": User_registration_Form,
            "respuesta": "Contraseñas no coinciden"
            })
      
               
def sigin(request):
    
    if request.method == "GET":
        print("Cargando datos")
        return render (request,"sigin.html", {
        "form": AuthenticationForm
        })
    
    else:
       
        user = request.POST["username"]
        front_password = request.POST["password"]
        
        if User.objects.filter(username=user).exists():
            True
            
            user_obj = User.objects.filter(username=user).first()
            queried_password = user_obj.password
            
            if check_password(front_password, queried_password):
                login(request, user_obj)
                return redirect("/new_task/")
            
            else:
                return render (request,"sigin.html", {
                    "form": AuthenticationForm,
                    "respuesta": "Contraseña incorrecta",
                })
        else:
            return render (request,"sigin.html", {
                "form": AuthenticationForm,
                "respuesta": "Usuario no registrado"
            })

       
@login_required
def signout(request):
    logout(request)
    return redirect ("/sigin/")


@login_required
def task (request):
    if request.method == "GET":
        tareas = Taks.objects.filter(user = request.user)
        return render (request, "task.html", {
        "taks":tareas
        })
        
    else:
        tareas = Taks.objects.filter(user = request.user)
        tareas.delete()
        return redirect ("/new_task/")
    
    
@login_required           
def new_task (request):
    user = User.objects.filter(username = request.user)
    
    if request.method == "GET":
        return render (request,"new_task.html", {
        "form": TaskForm,
        "user": user
        })
    
    else:
        try:
            print("Subiendo datos")
            form = TaskForm(request.POST)
            nueva_tarea = form.save(commit=False)
            nueva_tarea.user = request.user
            nueva_tarea.save()
            return redirect ("/task/")
        
        except ValueError:
            return render (request,"new_task.html", {
                "form": TaskForm,
            })
   
         
def task_delete(request, id):
    if request.method == "POST":
        task = Taks.objects.filter(id=id, user=request.user)
        task.delete()
    return redirect("/task/")