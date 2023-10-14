from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView
from admin_app.forms import *
from admin_app.models import *


class StartPageView(TemplateView):
    template_name = 'admin_app/start_page.html'


class AddRoomPageView(CreateView):
    model = Room
    template_name = 'admin_app/add_room_page.html'
    form_class = RoomModelForm
    success_url = reverse_lazy('admin_app:rooms')


class RoomsPageView(ListView):
    model = Room
    template_name = 'admin_app/rooms_page.html'
    context_object_name = 'rooms'


class BookApplicationsPageView(ListView):
    model = BookApplication
    template_name = 'admin_app/book_application_page.html'
    context_object_name = 'applications'


def is_hidden_true(request, slug_room):
    room = Room.objects.get(slug=slug_room)
    room.is_hidden = True
    room.save()
    return redirect('admin_app:rooms')


def is_hidden_false(request, slug_room):
    room = Room.objects.get(slug=slug_room)
    room.is_hidden = False
    room.save()
    return redirect('admin_app:rooms')


def approve_application(request, slug_book_application):
    application = BookApplication.objects.get(pk=slug_book_application)
    context = {'application': application}
    return render(request, 'admin_app/application_details_page.html', context)


def change_status(request, slug_book_application):
    application = get_object_or_404(BookApplication, pk=slug_book_application)
    room = Room.objects.get(pk=application.room_id.id)

    if request.method == 'POST':
        status = request.POST.get('status')
        if status == 'approve':
            application.approve_status = True
            room.reserved = True
            room.save()
        elif status == 'reject':
            application.approve_status = False
        application.save()

    return redirect('admin_app:book_applications')
