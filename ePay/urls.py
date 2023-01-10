from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    # Admin URLs to be commented ...
    path('admin/', admin.site.urls),

    # App Level Imported URLs ...
    path('api/users/', include('accounts.urls')),
    path('api/vendor/', include('vendor.urls')),
    path('api/customer/', include('customer.urls')),

    # Token for User Token Manipulation
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/tpken/verify/', TokenVerifyView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
