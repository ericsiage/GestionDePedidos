from django import forms
class formularioContacto(forms.Form):
    
    nombre = forms.CharField(label='Nombre', required=True, max_length=20)
    email = forms.CharField(label='Email', required=True, max_length=20)
    contenido = forms.CharField(label='Contenido', widget=forms.Textarea)