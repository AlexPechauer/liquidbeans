from django.shortcuts import render
from .models import Orders

def index(request):
    order_list = Orders.objects.order_by('drink')[:5]
    context = {'order_list': order_list}
    return render(request, 'coffee/index.html', context)
