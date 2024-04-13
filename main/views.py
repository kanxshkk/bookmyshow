
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm, BookingForm
from .models import User
from .models import Movie, ShowTiming, Booking

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def movie_listing(request):
    unique_languages = Movie.objects.values_list('language', flat=True).distinct()

    selected_language = request.GET.get('language')

    if selected_language:  
        movies = Movie.objects.filter(language=selected_language)
    else:  
        movies = Movie.objects.all()

    return render(request, 'movie_listing.html', {'movies': movies, 'unique_languages': unique_languages})



@login_required
def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    show_timings = ShowTiming.objects.filter(movie=movie)
    return render(request, 'movie_detail.html', {'movie': movie, 'show_timings': show_timings})

@login_required
def show_timing_selection(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    show_timings = ShowTiming.objects.filter(movie=movie)
    return render(request, 'show_timing_selection.html', {'movie': movie, 'show_timings': show_timings})

@login_required
def booking(request, show_timing_id):
    show_timing = get_object_or_404(ShowTiming, pk=show_timing_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            num_tickets = form.cleaned_data['num_tickets']
            if num_tickets > 0:
                # Check if there are enough available tickets
                if show_timing.available_tickets() >= num_tickets:
                    # Create a new booking
                    booking = Booking.objects.create(
                        user=request.user,
                        show_timing=show_timing,
                        num_tickets=num_tickets,
                        movie=show_timing.movie
                    )
                    # Redirect to the booking history page
                    return redirect('booking_history')
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'show_timing': show_timing, 'form': form})

@login_required
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking_history.html', {'bookings': bookings})
