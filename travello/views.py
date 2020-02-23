from django.shortcuts import render, redirect
from .models import Destination

# Create your views here.
def travello(request):

    destinations = Destination.objects.all()

    return render(request, 'index.html', {'dests': destinations})

def destination(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'destinations.html')
        else:
            return redirect('accounts/login')



