from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/tpken/verify/', TokenVerifyView.as_view()),
    # path('api-auth/', include('rest_framework.urls')),
    path('api/users/', include('accounts.urls')),
    # path('tags/', include('tags.urls')),
    # path('brands/', include('brand.urls')),
]
