from django.contrib import admin

# Register your models here.

#Campos created y updated son de solo lectura
class ProjectAdmin (admin.ModelAdmin):
    readonly_fields= ('created','updated')
admin.site.register(Proyectos)