from django.db import models

# Create your models here.
class Carrera(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        txt = "{0}(Duración: {1} año(s))"
        return txt.format(self.nombre, self.duracion)
    
class Estudiante(models.Model):
    dni = models.CharField(max_length=15, primary_key=True)
    apellidoPaterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    nombres = models.CharField(max_length=70)
    fechaNacimiento = models.DateField()
    generos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    genero = models.CharField(max_length=1, choices=generos, default='F')
    carrea= models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)

    def nombreCompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)
    
    def __str__(self):
        txt = "{0} / Carrera: {1} / {2}"
        if self.vigencia:
            estadoEstudiante = "VIGENTE"
        else:
            estadoEstudiante= "DE BAJA"
        return txt.format(self.nombreCompleto(), self.carrea, estadoEstudiante)

class Curso(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    docente = models.CharField(max_length=100)

class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante= models.ForeignKey(Estudiante, null=False, blank=False , on_delete=models.CASCADE)
    curso= models.ForeignKey(Curso, null=False, blank=False , on_delete=models.CASCADE)
    fechaMatricula= models.DateTimeField(auto_now_add=True)