from django.shortcuts import redirect, render, reverse
from django.http import JsonResponse
import stripe 
from django.contrib import messages

stripe.api_key = 'sk_test_uJRUYVikIfop3NiATOkOgr6f00VWrVdU9S'

def give(request):
    return render(request, 'give.html')

def charge(request):
    if request.method == 'POST':
        # print('Data:', request.POST)

        amount = int(request.POST['amount'])
        description = request.POST['description']
        name_cust = request.POST['name']

        customer = stripe.Customer.create(
            name = request.POST['name'],
            email =  request.POST['email'],
            description = request.POST['description'],
            source = request.POST['stripeToken']
        )

        charge = stripe.Charge.create(
            customer = customer,
            amount = amount*100,
            currency = 'usd',
            description = description
        )

        messages.success(request, f"{name_cust.title()}, thank you for your donation of ${amount}!")
        
    return redirect(reverse('give'))