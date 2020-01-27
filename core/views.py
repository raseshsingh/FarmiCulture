from django.shortcuts import render
from .models import Item


# Create your views here.

def index(request):
    return render(request, 'core/index.html')


def list_item(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'core/item_list.html', context)
