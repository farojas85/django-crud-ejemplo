from django import forms
from django.forms import widgets
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        model=Estudiante
        fields= ['dni','nombres','apellidos']
        labels={
            'dni': 'D.N.I.:','nombres':'Nombres',
            'apellidos': 'Apellidos'
        }
        widgets = {
            'dni':forms.TextInput,
            'nombres':forms.TextInput,
            'apellidos':forms.TextInput
        }

        def __init__(self,*args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'input'
                })
            pass