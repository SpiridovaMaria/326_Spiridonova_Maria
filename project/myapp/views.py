import hashlib

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from myapp.models import Passenger, Flights
from myapp.models import Passangers_and_Flights
from myapp.forms import TicketForm
from django.contrib.auth.models import User

# Create your views here.
def show_info(request):
    user = request.user
    if user.is_authenticated and user.groups.filter(name = "Customers").exists():
        passenger = Passenger.objects.get(id_user=user.id)
        flights = Passangers_and_Flights.objects.filter(id_passenger = passenger.passport)
        return render(request, 'passanger_info.html', {"passenger":passenger, "link_img": hashlib.md5(User.objects.get(id=passenger.id_user_id).email.encode('utf-8')).hexdigest(), "flights":flights, "is_manager":False})
    else:
        return redirect("/")
def show_passenger_card(request, number_flight, passport):
    user = request.user
    if user.is_authenticated and user.groups.filter(name = "Managers").exists():
        passenger = Passenger.objects.get(passport=str(passport))
        flights = Passangers_and_Flights.objects.filter(id_passenger=passenger.passport)
        return render(request, 'passanger_info.html', {"passenger":passenger, "link_img": hashlib.md5(User.objects.get(id=passenger.id_user_id).email.encode('utf-8')).hexdigest(), "flights":flights, "is_manager":True})
    else:
        return redirect("/")
def show_index(request):
    if request.method == "GET":
        cur_user = request.user
        if cur_user.is_authenticated and cur_user.groups.filter(name = "Customers").exists():
            return redirect("/info")
        elif cur_user.is_authenticated and cur_user.groups.filter(name = "Managers").exists():
            return redirect("/manager_info")
        else:
            return render(request,'index.html',{})
    else:
        if request.POST.get("email")!=None:
            try:
                email = request.POST.get("email")
                password = request.POST.get("password")
                username = User.objects.get(email=email).username
                user = authenticate(username=username, password=password)
                login(request, user)
                if user.groups.filter(name="Customers").exists():
                    return redirect("/info")
                else:
                    return redirect("/manager_info")
            except Exception:
                print("Email or password is incorrect.")
                return redirect("/")
        else:
            user = User.objects.create_user(email = request.POST.get("create_email"), username=request.POST.get("create_passport"),
                                            password = request.POST.get("create_pswd"))
            user.groups.add(1)
            passanger = Passenger(name = request.POST.get("create_name"), surname=request.POST.get("create_surname"),
                                  passport=request.POST.get("create_passport"), date_of_birth=request.POST.get("create_birthdate"),
                                  patronymic=request.POST.get("create_patronymic"), id_user_id=user.id)
            passanger.save()
            login(request, user)
            return redirect("/info")


def buy_ticket(request):
    if request.method=="GET":
        ticketForm = TicketForm()
        return render(request,'formTicket.html',{"form":ticketForm})
    else:
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit = False)
            ticket.id = Passangers_and_Flights.objects.all().last().id + 1
            ticket.id_passenger = Passenger.objects.get(id_user_id = request.user)
            services = form.cleaned_data["extra_service"]
            ticket.save()
            for service in services:
                ticket.extra_service.add(service)
            return redirect("/info/")
        else:
            print("ups")
            return redirect("/")
def delete_ticket(request, number_flight, passport, id_ticket):
    passenger = Passenger.objects.get(passport = passport)
    Passangers_and_Flights.objects.get(id = id_ticket, id_flight=number_flight, id_passenger= passenger.passport).delete()
    return redirect("/")
def show_manager_info(request):
    user = request.user
    if user.is_authenticated and user.groups.filter(name = "Managers").exists():
        flights = Flights.objects.all()
        return render(request, 'manager_info.html', {"flights": flights})
    else:
        return redirect("/")
def show_flight_info(request,number_flight):
    user = request.user
    if user.is_authenticated and user.groups.filter(name = "Managers").exists():
        flight = Flights.objects.get(number_flight=str(number_flight))
        passengers = Passangers_and_Flights.objects.all().filter(id_flight = str(number_flight))
        return render(request, 'flight_info.html', {"flight":flight, "passengers":passengers, "number_of_passengers": len(passengers)})
    else:
        return redirect("/")

#ajax view
def validate_passport(request):
    passport = int(request.GET.get("create_passport", None))
    if passport=='':
        passport=0
    print(passport)
    response = {
        'taken': Passenger.objects.filter(passport__exact=passport).exists()
    }
    return JsonResponse(response)
def validate_email(request):
    email = request.GET.get("create_email", None)
    response = {
        'exists': User.objects.filter(email__exact=email).exists()
    }
    return JsonResponse(response)
def validate_flight(request):
    flight = request.GET.getlist('id_flight', None)
    print(flight)
    response = {
        'exists': Passangers_and_Flights.objects.filter(id_passenger=Passenger.objects.get(id_user_id = request.user),id_flight=flight[0]).exists()
    }
    return JsonResponse(response)