from django.db import models

# Create your models here.
class Alumnos(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    cui = models.CharField(max_length=8, primary_key=True)
    numero = models.CharField(max_length=12, null=True)
    correo = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.cui} - {self.apellidos}, {self.nombres}"
class Curso(models.Model):
    nombre = models.CharField(max_length=15)
    id_curso = models.SmallIntegerField(primary_key=True, serialize=True)
    descripcion = models.TextField(null=True)
    docente = models.SmallIntegerField(null=True) #Se puede agregar el modelo docente para hacer mas completo el sistema
    def __str__(self):
        return self.nombre
class NotasAlumnosPorCurso(models.Model):
    alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=4, decimal_places=2)
    def __str__(self):
        return f"Alumno: {self.alumno.cui}, {self.curso.nombre} - {self.nota}"
    