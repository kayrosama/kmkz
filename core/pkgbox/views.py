from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

class KsmUno(View):
    def get(self, request):
        return render(request,'kmkz00.html')
    