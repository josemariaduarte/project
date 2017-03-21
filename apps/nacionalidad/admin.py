from django.contrib import admin

# Register your models here.
from apps.nacionalidad.models import Nacionalidad

class NacionalidadAdmin(admin.ModelAdmin):
    list_display = ['nombre','habilitado']
    list_filter = ('habilitado',)  #buscador
    search_fields = ('nombre',)
    list_per_page = 5  #a cada 5 elementos la paginacion


admin.site.register(Nacionalidad,NacionalidadAdmin)