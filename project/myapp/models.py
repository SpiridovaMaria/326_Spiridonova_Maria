from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Airline(models.Model):
    code = models.CharField(max_length=20, primary_key=True, verbose_name="код авиакомпании",
                            help_text="Введите код авиакомпании", null=False,
                            blank=False)
    name = models.CharField(max_length=100, verbose_name='название авиакомпании',
                            help_text="Введите название авиакомпании", null=False,
                            blank=False)
    type = models.CharField(max_length=200, verbose_name='тип', help_text="Введите тип авиакомпании", null=False,
                            blank=False)
    fleet_size = models.IntegerField(verbose_name='размер флота', help_text="Введите рамзер флота", null=False,
                                     blank=False)
    parent_company = models.CharField(max_length=100, verbose_name='материнская компания',
                                      help_text="Введите материнскую компанию", null=True, blank=True)

    def __str__(self):
        return "Авиакомпания " + self.name

    class Meta:
        db_table = "Airline"


class Flights(models.Model):
    number_flight = models.CharField(max_length=50, primary_key=True, verbose_name='номер рейса',
                                     help_text="Введите номер рейса",
                                     null=False, blank=False)
    destination = models.CharField(max_length=100, verbose_name="пункт назначения",
                                   help_text="Введите пункт назначения.", null=False, blank=False)
    date_of_flight = models.DateField(verbose_name="дата рейса", help_text="Введите дату рейса", null=False,
                                      blank=False)
    time_flight = models.TimeField(verbose_name="время вылета", help_text="Введите время вылета", null=False,
                                   blank=False)
    check_in = models.CharField(max_length=100, verbose_name="стойки регистрации",
                                help_text="Введите стойки регистрации", null=True, blank=True)
    registration = models.BooleanField(verbose_name="регистрация", help_text="Регистрация на рейс началась?",
                                       null=False, blank=False)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, verbose_name="airline",
                                help_text="Выберите авиакомпанию, совершающую рейс", null=True, blank=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="id рейса", help_text="Введите id рейса",
                                null=True, blank=True)

    def __str__(self):
        return "Рейс " + self.number_flight

    class Meta:
        db_table = "Flight"


class Passenger(models.Model):
    passport = models.BigIntegerField(primary_key=True, verbose_name='номер паспорта',
                                      help_text="Введите номер пасспорта",
                                      null=False, blank=False)
    name = models.CharField(max_length=50, verbose_name='имя', help_text="Введите имя пассажира", null=False,
                            blank=False)
    surname = models.CharField(max_length=100, verbose_name='фамилия', help_text="Введите фамилию",
                               null=False, blank=False)
    patronymic = models.CharField(max_length=100, verbose_name='отчество', help_text="Введите отчество",
                                  null=True, blank=True)
    date_of_birth = models.DateField(verbose_name='дата рождения', help_text="Введите дату рождения", null=False,
                                     blank=False)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="id пассажира",
                                help_text="Введите id пассажира",
                                null=True, blank=True)

    def __str__(self):
        return "Пассажир " + self.name + " " + self.surname

    class Meta:
        db_table = "Passanger"


class Extra_service(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="id", help_text="Введите id", null=False, blank=False)
    service_name = models.CharField(max_length=50, verbose_name='Название услуги', help_text="Введите название услуги", null=False,
                            blank=False)
    def __str__(self):
        return "Услуга " + self.service_name

    class Meta:
        db_table = "Extra_service"

class Passangers_and_Flights(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id", help_text="Введите id", null=False, blank=False)
    id_flight = models.ForeignKey(Flights, on_delete=models.CASCADE, verbose_name="flight", help_text="Выберите рейс",
                                  null=False, blank=False, default="PD 6543")
    id_passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, verbose_name="passenger",
                                     help_text="Выберите пассажира",
                                     null=False, blank=False)
    with_baggage = models.BooleanField(verbose_name='багаж', help_text="Пассажир летит с багажом?", null=False,
                                       blank=True, default=False)
    baggage_weight = models.IntegerField(verbose_name="вес багажа", help_text="Введите вес багажа", null=True, blank=True, default=0)
    extra_service = models.ManyToManyField(Extra_service,verbose_name="дополнительные услуги", help_text="Выберите дополнительные услуги", null = True, blank=True)
    def __str__(self):
        return "Пассажир " + self.id_passenger.surname + " рейс "+self.id_flight.number_flight

    class Meta:
        db_table = "Passangers_and_fligths"


from django.db import models

# Create your models here.
