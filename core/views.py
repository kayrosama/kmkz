from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

class KsmDos(View):
    def get(self, request):
        return render(request,'kmkz01.html')
