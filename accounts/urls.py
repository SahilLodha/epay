from django.urls import path
from .views import RetrieveUserView

urlpatterns = [
    path('', RetrieveUserView.as_view())
]

