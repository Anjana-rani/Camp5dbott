

# ottapp/urls.py
from django.urls import path
from .views import home, login_view, trinex_view, registration_view

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('trinex/',trinex_view,name='trinex'),
    path('registration/', registration_view, name='registration'),

]




