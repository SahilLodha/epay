from django.urls import path
from .views import VendorRegisterView

urlpatterns = [
    path('register', VendorRegisterView.as_view()),
]

