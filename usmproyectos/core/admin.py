from django.contrib import admin

from .models import Estudiante
from .models import Profesor
from .models import Proyecto
# Register your models here.

admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Proyecto)