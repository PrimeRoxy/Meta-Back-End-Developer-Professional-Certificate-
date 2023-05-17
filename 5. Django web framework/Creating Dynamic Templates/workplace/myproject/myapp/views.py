from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu

# Create your views here for menu.
def menu(request):
    menu_items = Menu.objects.all()
    item_dic = {'menu': menu_items}
    return render(request, 'menu.html', item_dic)