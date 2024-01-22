# techwaveapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Customer, TechSupportService, CybercafeUsage, TrainingProgram
from .forms import ContactForm
from .models import Ticket
from .forms import TicketForm


def index(request):
    customers = Customer.objects.all()
    services = TechSupportService.objects.all()
    cafe_usage_records = CybercafeUsage.objects.all()
    training_programs = TrainingProgram.objects.all()
    return render(request, 'techwaveapp/index.html', {
        'customers': customers, 
        'services': services,
        'cafe_usage_records': cafe_usage_records,
        'training_programs': training_programs,
    })

def services(request):
    # Query all services from the database
    services = TechSupportService.objects.all()
    
    # Pass the services data to the template
    context = {'services': services}
    
    return render(request, 'services.html', context) 
        
def cafe_usage_view(request):
    cafe_usage_records = CybercafeUsage.objects.all()
    return render(request, 'techwaveapp/cafe_usage.html', {'cafe_usage_records': cafe_usage_records})

def training_programs_view(request):
    training_programs = TrainingProgram.objects.all()
    return render(request, 'techwaveapp/training_programs.html', {'training_programs': training_programs})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the homepage after successful submission
    else:
        form = ContactForm()

    return render(request, 'techwaveapp/contact.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
def ticket_list(request):
    tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'techwaveapp/ticket_list.html', {'tickets': tickets})

@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('ticket_list')
    else:
        form = TicketForm()
    return render(request, 'techwaveapp/create_ticket.html', {'form': form})

@login_required
def ticket_detail(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id, user=request.user)
    return render(request, 'techwaveapp/ticket_detail.html', {'ticket': ticket})

