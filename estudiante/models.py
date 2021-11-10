from django.db import models

# Create your models here.
class Estudiante(models.Model):
    id = models.BigAutoField(primary_key=True,verbose_name="ID")
    dni = models.CharField(max_length=8,help_text="DNI Estudiante")
    nombres = models.CharField(max_length=191,help_text="Nombres")
    apellidos= models.CharField(max_length=191,help_text="Apellidos")

    class Meta:
        verbose_name_plural ='estudiantes'
    
    def __str__(self) -> str:
        return '{0} {1}'.format(self.nombres,self.apellidos)

