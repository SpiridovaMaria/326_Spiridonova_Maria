"""
URL configuration for laba_4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', views.show_info),
    path('ajax/validate_passport/',views.validate_passport, name='validate_passport'),
    path('ajax/validate_email/',views.validate_email, name='validate_email'),
    path('flight_info/<str:number_flight>/info/<str:passport>/', views.show_passenger_card, name = 'show_passenger'),
    path('', views.show_index, name="home"),
    path('buyticket/',views.buy_ticket, name="buyticket"),
    path('flight_info/<str:number_flight>/info/<str:passport>/<int:id_ticket>/deleteticket', views.delete_ticket, name="deleteTicket"),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy("home")), name='logout'),
    path('manager_info/', views.show_manager_info),
    path('flight_info/<str:number_flight>/', views.show_flight_info),
    path('ajax/validate_flight/',views.validate_flight, name='validate_flight'),

]