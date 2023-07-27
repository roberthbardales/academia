from django.db import models

from django.contrib.auth.models import User
# CURSOS

class Course(models.Model):

    name = models.CharField(max_length=90, verbose_name='Nombre')
    description = models.TextField(blank=True, null=True, verbose_name='Descripcion')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name':'profesores'}, verbose_name='Profesor')
    class_quantity=models.PositiveIntegerField(default=0,verbose_name='Cantidad de Clases')


    def __str__(self):
        return self.name
    class Meta:

        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

# INSCRIPCIONES

class Registration(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE,verbose_name='Curso')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stundents_registration',
                                limit_choices_to={'groups__name':'estudiantes'}, verbose_name='Estudiante')
    enabled = models.BooleanField(default=True, verbose_name='Alumno Regular')

    def __str__(self):
        return f'{self.student.username}-{self.course.name}'

    class Meta:

        verbose_name = 'Inscripcion'
        verbose_name_plural = 'Inscripciones'


# Asistencias
class Attendance(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE,verbose_name='Curso')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attendances',
                                limit_choices_to={'groups__name':'estudiantes'}, verbose_name='Estudiante')
    present = models.BooleanField(default=False,blank=True,null=True,verbose_name='Presente')
    date = models.DateField(null=True,blank=True, verbose_name='Fecha')

    def __str__(self):
        return f'Asistencia{self.id}'

    # logica para generar el estado del alumno regular/ irregular(enabled)
    # total-asistencias => class_quantity del modelo course
    # total-inasistencias =>present=False
    # porcentaje de inasistencias=(total-inasistencias/total-clases) *100 ----------> >20(>20%) =>alumno es irregular =>enabled = False
    # total-clases=10


    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'

# Notas
class Mark(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE,verbose_name='Curso')
    student = models.ForeignKey(User, on_delete=models.CASCADE,
                                limit_choices_to={'groups__name':'estudiantes'}, verbose_name='Estudiante')
    mark_1 = models.IntegerField(null=True,blank=True, verbose_name='Nota 1')
    mark_2 = models.IntegerField(null=True,blank=True, verbose_name='Nota 2')
    mark_3 = models.IntegerField(null=True,blank=True, verbose_name='Nota 3')
    average = models.DecimalField(max_digits=3, decimal_places=1,null=True,blank=True,verbose_name='Promedio')

    def __str__(self):
        return str(self.course)

    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencia'

    # Calcular el Promedio
    def calculate_average(self):
        marks=[self.mark_1,self.mark_2, self.mark_3]
        valid_marks=[mark for mark in marks if mark is not None]
        if valid_marks:
            return sum(valid_marks)/len(valid_marks)
        return None

    def save(self,*args,**kwargs):
        # verifico si alguna nota cambio
        if self.mark_1 or self.mark_2 or self.mark_3:
            self.average=self.calculate_average()       # calulcar le promedio(llamo a una funcion)
        super().save(*args,**kwargs)

    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'



