from django import forms
from crud.models import Taks


class TaskForm (forms.ModelForm):
    class Meta:
        model = Taks
        fields = ['title', 'description', 'important',]
        


class User_registration_Form(forms.Form):
    first_name = forms.CharField(label="Nombre",max_length=20)
    last_name = forms.CharField(label="Apellido",max_length=20)
    username = forms.CharField(label="Nombre de usuario",max_length=15)
    email = forms.EmailField(label="Correo",max_length=254,required=True)
    
    password_1 = forms.CharField(label="Contraseña",max_length=30 ,widget=forms.PasswordInput())
    password_2 = forms.CharField(label="Confirmar contraseña",max_length=30 ,widget=forms.PasswordInput())
    


class EmailVerificationForm (forms.Form):
    email = forms.EmailField(label="correo electronico",max_length=254, required= True)