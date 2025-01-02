from django.contrib import admin
from pkgbox.models import Guia

@admin.register(Guia)
class GuiaAdmin(admin.ModelAdmin):
    list_display = ['empresa','idguia','srcfecha','regsts','fecha_reg','fecha_mod']
    