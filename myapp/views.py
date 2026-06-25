# myapp/views.py
from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages
from .models import Booking 
from datetime import datetime
from .models import Hotel
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .forms import BookingForm
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse



def index(request):
    return render(request, 'index.html')



def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email, password=password)
            return redirect('hotel')
        except User.DoesNotExist:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=request.POST['password'],
        )
        messages.success(request, 'Signup successful! Please login.')
        return redirect('login')
    return render(request, 'signup.html')

def hotel(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel.html', {'hotels': hotels})


def home_view(request):
    return render(request, 'home.html')



def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    return render(request, 'room-detail.html', {'hotel': hotel})
def booking_view(request):
    if request.method == "POST":
        hotel_name = request.POST.get('hotel_name', 'Hotel Unknown')  # ✅
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        checkin = request.POST.get('check_in')
        checkout = request.POST.get('check_out')
        guests = int(request.POST.get('guests', 1))
        room_type = request.POST.get('room_type')

        checkin_date = datetime.strptime(checkin, "%Y-%m-%d").date()
        checkout_date = datetime.strptime(checkout, "%Y-%m-%d").date()
        nights = (checkout_date - checkin_date).days

        rate_per_night = {
            'Single': 1000,
            'Double': 1500,
            'Suite': 2500
        }.get(room_type, 1000)

        total_amount = nights * rate_per_night

        booking = Booking.objects.create(
            hotel_name=hotel_name,  # ✅ set it here
            name=name,
            email=email,
            checkin=checkin,
            checkout=checkout,
            guests=guests,
            room_type=room_type,
            total_amount=total_amount
        )

        return redirect('booking_confirm', booking_id=booking.id)

    return render(request, 'booking.html')



def booking_confirm(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'booking_success.html', {'booking': booking})

def booking_pdf(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    nights = (booking.checkout - booking.checkin).days
    html = get_template('booking_pdf.html').render({
        'booking': booking,
        'nights': nights
    })
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename="booking_{booking.id}.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)
    return response
