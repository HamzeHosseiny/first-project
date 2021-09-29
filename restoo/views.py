from django.shortcuts import render

def home(request):
    return render(request, 'restoo/index.html')
