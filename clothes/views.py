import datetime

from django.shortcuts import render, redirect
from django.contrib import messages

from django.http import HttpResponse
from .models import Product, BookProduct

# Create your views here.


def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, "index.html", context)


def check_bookings(request, pk):
    print("dd")
    user = request.user
    product = Product.objects.get(id=pk)
    currentdate = datetime.datetime.today().strftime('%Y-%m-%d')
    if request.method == "POST":
        rent_from = request.POST['rentfrom']
        rent_to = request.POST['rentto']
        print("done")
        if rent_from < currentdate:
            messages.info(request, "check the selected date")
            return redirect('index')
        else:
            filter_params = dict(rent_from__lte=rent_from, rent_to__gte=rent_from)
            is_booked_check1 = BookProduct.objects.filter(**filter_params, product=product).exists()

            filter_params2 = dict(rent_from__lte=rent_to, rent_to__gte=rent_to)
            is_booked_check2 = BookProduct.objects.filter(**filter_params2, product=product).exists()
            print(is_booked_check1, is_booked_check2)
            if is_booked_check1 or is_booked_check2:
                print("already booked")
                messages.info(request, "Already booked for the date")
                return redirect('index')
            else:
                BookProduct.objects.create(
                    user=user,
                    product=product,
                    rent_from=rent_from,
                    rent_to=rent_to
                )
                print(rent_from, rent_to)
                messages.info(request, "Your Booking Was Successfull!!!")
                return redirect('index')


def create_booking(request):
    return render(request, 'create_booking.html')