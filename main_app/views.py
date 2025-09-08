from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# Define the home view function
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
    return render(request, 'about.html')

def test(request):
    return HttpResponse('<h1>TEST PAGE SUCCESS</h1>')
