from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'service-details.html')

def portfolio(request):
    return render(request, 'portfolio-details.html')

def starter(request):
    return render(request, 'starter-page.html')

# Create your views here.
