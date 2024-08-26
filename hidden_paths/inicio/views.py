from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import TourBooking
from django.urls import reverse
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth.views import PasswordResetView
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from .models import Tours
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ReviewForm
from .forms import CustomLoginForm, CustomUserCreationForm
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from .models import Review
from datetime import date




def Principal(request):
    return render(request, 'principal.html')
    

def tours(request):
    success = request.GET.get('success')
    tour_id = request.GET.get('tour_id')
    tour = None
    if tour_id:
        tour = TourBooking.objects.get(id=tour_id)
    return render(request, 'inicio/tours.html', {
        'success': success,
        'tour': tour
    })

def realizados(request):
    hoy = date.today()
    tours = Tours.objects.filter(fecha__lt=hoy)
    return render(request,"inicio/realizados.html",{"tours":tours})
                  
def tours_list(request):
    hoy = date.today()
    tours = Tours.objects.filter(fecha__gt=hoy) # Obtener todos los tours
    return render(request, 'inicio/Tours.html', {'tours': tours})


def tours_view(request):
    tours = Tours.objects.all().prefetch_related('reviews')
    context = {
        'tours': tours,
    }
    return render(request, 'Tours.html', context)


def Conocenos(request):
    return render(request, "inicio/Conocenos.html")


def Login(request):
    if request.method == "POST":
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('principal')  # Redirige al menú principal si la autenticación es exitosa
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos')
    else:
        form = CustomLoginForm()

    return render(request, 'Registros/Login.html', {'form': form})


def CrearCuenta(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Tu cuenta ha sido creada exitosamente.")
            return redirect('Principal')  # Redirect to the main page
    else:
        form = CustomUserCreationForm()
    return render(request, 'Registros/CrearCuenta.html', {'form': form})


def Agendar(request):
    if request.method == 'POST':
        # Aquí guardas los datos del tour en la base de datos
        tour_data = {
            'nombre': request.POST['nombre'],
            'email': request.POST['email'],
            'numero_telefonico': request.POST['numero_telefonico'],
            'fecha': request.POST['fecha'],
            'hora': request.POST['hora'],
            'num_personas': request.POST['num_personas'],
            'tipo_tour': request.POST['tipo_tour'],
        }
        tour_booking = TourBooking.objects.create(**tour_data)
        # Redirigir a la página de pago
        return redirect(reverse('Payment') + f'?tour_id={tour_booking.id}')
    return render(request, 'tours/Agendar.html')


def payment(request):
    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvv = request.POST.get('cvv')
        tour_id = request.session.get('tour_id')  # Obtener el ID del tour desde la sesión

        # Aquí debes agregar la lógica para procesar el pago

        # Suponiendo que el pago y la reserva del tour se completan con éxito
        messages.success(request, 'Tu tour fue pagado y agendado con éxito.')
        return redirect('Tours')  # Redirige a la vista de tours con el mensaje de éxito

    return render(request, 'tours/payment.html')





@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


def some_view(request):
    if request.user.is_authenticated:
        # Usuario está autenticado
        username = request.user.username
        # Realiza operaciones con la información del usuario
    else:
        # Usuario no está autenticado
        pass

def Reviews_view(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'tours/Reviews_view.html', context)


def crear_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  # Asigna el usuario actual al campo `user`
            review.save()
            return redirect('reviews')  # Redirige a la vista de reviews después de guardar
    else:
        form = ReviewForm()
    return render(request, 'tours/crear_review.html', {'form': form})

