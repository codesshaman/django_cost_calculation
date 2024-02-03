from django.urls import path
from .views import home, rules, loss


urlpatterns = [
    path('', home),
    path('rules', rules),
    path('loss', loss)
]
