from django import forms
from django.db import models
from .models import Review, Tours
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['tour', 'rating', 'comment']

    tour = forms.ModelChoiceField(queryset=Tours.objects.all(), empty_label="Seleccione un tour")
    rating = forms.IntegerField(min_value=1, max_value=5, widget=forms.NumberInput(attrs={'placeholder': 'Calificación (1-5)'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Escriba su comentario'}))
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'accept': 'image/*'}))

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Nombre de usuario',
        max_length=254,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        label='Nombre',
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        label='Apellidos',
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['tour', 'rating', 'comment', 'image'] 

    

