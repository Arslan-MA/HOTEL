from django.urls import path
from client_app.views import *

app_name = 'client_app'

urlpatterns = [
    path('', StartPageView.as_view(), name='start_page'),
    path('rooms/', RoomsPageView.as_view(), name='rooms'),
    path('rooms/<slug_room>/', room_detail_page, name='room_detail'),
    path('rooms/<slug_room>/likes/', likes_room, name='likes_room'),
    path('rooms/<slug_room>/book-application/', booking_request_page, name='booking_request'),
    path('books/', application_list, name='application_page'),
    path('books/<slug_book_application>', cancel_request, name='cancel_request'),
]
