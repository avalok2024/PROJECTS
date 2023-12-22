import phonenumbers
from phonenumbers import timezone,carrier,geocoder

number = input("Enter the number with +__ : ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")
print(phone)
print(time)
print(reg)
print(car)
