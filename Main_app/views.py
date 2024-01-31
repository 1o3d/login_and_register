from django.shortcuts import render


# Create your views here.



def home(request):
    return render(request, 'Main_app/home.html')


def child(request):
    return render(request, 'Main_app/child.html')