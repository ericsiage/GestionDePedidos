from django import forms
class formularioContacto(forms.Form):
    
    nombre = forms.CharField(label='Nombre', required=True, max_length=20)
    email = forms.EmailField(label='Email', required=True, max_length=100)
    asunto = forms.CharField(label='Asunto', required=True, max_length=20)
    contenido = forms.CharField(label='Contenido', widget=forms.Textarea)