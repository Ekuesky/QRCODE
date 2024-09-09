from django.urls import path
from .views import generate_qr_code, index

urlpatterns = [
    path('', index, name='index'),
    path('generate/', generate_qr_code, name='generate-qr-code'),
]