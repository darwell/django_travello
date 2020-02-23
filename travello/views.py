from django.shortcuts import render
from .models import Destination

# Create your views here.
def travello(request):

    destinations = Destination.objects.all()

    return render(request, 'index.html', {'dests': destinations})
