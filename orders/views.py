from django.shortcuts import render
from .models import Customer

def clerck(request):
    return render(request, "clerck.html")

def clerck_add_customer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        print(name)
        print(phone)
        customer = Customer()
        customer.name = name
        customer.phone = phone
        customer.save()
        
    return render(request, "clerck_add_customer.html")
