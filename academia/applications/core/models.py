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

