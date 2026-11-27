from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def person(request):
    return render(request, 'person.html')

def logout(request):
    return render(request, 'accounts/logout.html')
