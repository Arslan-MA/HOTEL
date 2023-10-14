from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from admin_app.forms import *
from admin_app.models import *


class StartPageView(TemplateView):
    template_name = 'client_app/start_page.html'


class RoomsPageView(ListView):
    model = Room
    template_name = 'client_app/rooms_page.html'
    context_object_name = 'rooms'


class RoomDetailPageView(DetailView):
    model = Room
    template_name = 'client_app/room_detail_page.html'
    slug_url_kwarg = 'slug_room'
    context_object_name = 'room'


def room_detail_page(request, slug_room):
    room = Room.objects.get(slug=slug_room)
    if request.method == "POST":
        form = CommentModelForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            content = form.cleaned_data['content']
            comment = Comment.objects.create(author=author,
                                             content=content)
            room.comment = comment
            room.save()

        return redirect('client_app:rooms')
    else:
        form = CommentModelForm()
    context = {'room': room,
               'comments': Comment.objects.all(),
               'form': form}

    return render(request, 'client_app/room_detail_page.html', context)


# def comment_fun(request, slug_room):
#     room = Room.objects.get(slug=slug_room)
#     if request.method == "POST":
#         form = CommentModelForm(request.POST)
#         if form.is_valid():
#             author = form.cleaned_data['author']
#             content = form.cleaned_data['content']
#             comment = Comment.objects.create(author=author,
#                                              content=content)
#             room.comment = comment
#             room.save()
#
#     return redirect('admin_app:rooms.html')


def booking_request_page(request, slug_room):
    room = Room.objects.get(slug=slug_room)
    if request.method == 'POST':
        form = BookApplicationForm(request.POST)
        if form.is_valid():
            client = Client(first_name=request.POST.get('first_name'),
                            last_name=request.POST.get('last_name'),
                            middle_name=request.POST.get('middle_name'),
                            email=request.POST.get('email'))
            client.save()

            book_application = BookApplication(client_id=client,
                                               room_id=room,
                                               number_persons=form.cleaned_data['number_persons'],
                                               start_book=form.cleaned_data['start_book'],
                                               end_book=form.cleaned_data['end_book'])
            book_application.save()

            services = form.cleaned_data['services']
            for service_id in services:
                book_application.services.add(service_id)
            book_application.calculate_total_price()
            book_application.save()

            return redirect('client_app:start_page')
    else:
        form = BookApplicationForm()

    return render(request, 'client_app/booking_request_page.html', {'form': form})


def likes_room(request, slug_room):
    room = Room.objects.get(slug=slug_room)
    room.likes += 1
    room.save()
    return redirect('client_app:rooms')


def application_list(request):
    application = BookApplication.objects.all()
    if application.exists():
        return render(request, 'client_app/application_page.html', {'applications': application})
    else:
        return redirect('client_app:rooms')


def cancel_request(request, slug_book_application):
    request = BookApplication.objects.get(pk=slug_book_application)
    request.delete()
    return redirect('client_app:rooms')
