from django.shortcuts import render


def index(request):
    return render(request, 'project0/index.html')
