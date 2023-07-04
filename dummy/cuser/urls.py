from .views import SignUp
from django.urls import path,include

urlpatterns = [
    path('register',SignUp.as_view(),name='regs'),
]
