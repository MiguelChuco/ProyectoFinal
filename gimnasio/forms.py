from django import forms

class ActividadForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    descripcion = forms.CharField(widget=forms.Textarea)

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    precio = forms.DecimalField()
    descripcion = forms.CharField(widget=forms.Textarea)

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)
