from django.shortcuts import render
from .models import MenuItem

def index(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'myapp/index.html', {'menu_items': menu_items})
