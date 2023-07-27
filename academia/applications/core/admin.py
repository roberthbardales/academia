from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'teacher',
        'class_quantity',
                    )
    list_filter = (
        'teacher',
        )
admin.site.register(Course,CourseAdmin)