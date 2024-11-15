from django.contrib import admin
from core.pkgbox.models import Guia

@admin.register(Guia)
class GuiaAdmin(admin.ModelAdmin):
    list_display = ['regid','idguia','srcfecha','regsts','fecha_reg','fecha_mod']
    