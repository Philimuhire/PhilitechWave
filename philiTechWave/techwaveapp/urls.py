# techwaveapp/urls.py

from django.contrib import admin
from django.urls import path, include
from . import views
from .views import index, cafe_usage_view, training_programs_view, contact_view, register_view
from .views import ticket_list, create_ticket, ticket_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('services/', views.services, name='services'),
    path('cafe-usage/', cafe_usage_view, name='cafe_usage'),
    path('training-programs/', training_programs_view, name='training_programs'),
    path('contact/', contact_view, name='contact'),
    path('accounts/', include('django.contrib.auth.urls')),  # Include default authentication views
    path('accounts/register/', register_view, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),  # Include default authentication views
    path('tickets/', ticket_list, name='ticket_list'),
    path('tickets/create/', create_ticket, name='create_ticket'),
    path('tickets/<int:ticket_id>/', ticket_detail, name='ticket_detail'),
]
