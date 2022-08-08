from django.contrib import admin
from app.models import Package, UserRegister,PaymentDetails
# from PassengerAPI.models import *
# from taxi.models import *
# Register your models here.
admin.site.register(UserRegister)
#admin.site.register(PersonalDetails)
admin.site.register(PaymentDetails)
admin.site.register(Package)
# admin.site.register(Passenger)
# admin.site.register(TravelHistory)
# admin.site.register(Driver)
# admin.site.register(DriverLocation)
# admin.site.register(DriverRiderHistory)

