
def home(request):
    return render(request, 'user/home.html')





from django.contrib.auth import authenticate, login

from django.http import HttpResponse
from .forms import MyLoginForm
from .models import Customer


def login_view(request):
    if request.method == 'POST':
        login_form = MyLoginForm(request.POST)
        if login_form.is_valid():
            cleaned_data = login_form.cleaned_data
            username = cleaned_data['username']
            password = cleaned_data['password']

            # You can retrieve the customer data without authenticating
            try:
                customer = Customer.objects.get(username=username, password=password)
                # Do something with the customer data
                return redirect('trinex')
            except Customer.DoesNotExist:
                return HttpResponse('<h1>Not Authenticated</h1>')

    else:
        login_form = MyLoginForm()

    return render(request, template_name='user/login.html', context={'login_form': login_form})

def trinex_view(request):
    return render(request, 'trinex/trinex.html')



from django.shortcuts import render, redirect
from .forms import CustomerRegistrationForm

def registration_view(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.renew_membership(form.cleaned_data['payment_method'])
            customer.save()
            # Redirect to the login page or any other page you want
            return redirect('login')
    else:
        form = CustomerRegistrationForm()

    return render(request, 'user/registration.html', {'form': form})
