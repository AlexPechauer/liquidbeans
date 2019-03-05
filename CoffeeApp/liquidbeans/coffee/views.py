from django.shortcuts import render, redirect
from .models import Orders, DrinkChoice, Keyword
from .forms import CardForm
from django.contrib import messages
import datetime
from django.core.mail import EmailMessage

def index(request):
    order_list = Orders.objects.order_by('drink')
    keyword_list = Keyword.objects.order_by('-id')
    for keyword in keyword_list:
        correct_keyword = keyword.keyword
    if request.method =='POST':
        form = CardForm(request.POST)
        if form.is_valid():
            keyword_answer = form.cleaned_data.get('keyword')
            if correct_keyword == keyword_answer:
                name = form.cleaned_data.get('name')
                choice = request.POST.get('drink_order')
                keyword = keyword_answer
                select_date = datetime.datetime.now()
                customize = form.cleaned_data.get('customize')
                flavor_choice = request.POST.get('gridRadios')
                final = DrinkChoice(select_date = select_date, choice = choice, name = name, keyword = keyword, flavor_choice = flavor_choice, customize = customize)
                final.save()
                email = EmailMessage('{} wants a {}'.format(name, choice), '{} wants a {} with {}. Customization: {}'.format(name, choice, flavor_choice, customize), to=['apechauer@gmail.com'])
                email.send()
                messages.success(request, 'Your {} is on the way {}!'.format(choice, name))
                return redirect('index')
            else:
                messages.warning(request, 'Drink not submitted: Please enter the correct keyword')
    else:
        form = CardForm()
    context = {'order_list': order_list, 'form': form}
    return render(request, 'coffee/index.html', context)
