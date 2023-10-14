from django.urls import path
from admin_app.views import *

app_name = 'admin_app'

urlpatterns = [
    path('', StartPageView.as_view(), name='start_page'),
    path('add-room/', AddRoomPageView.as_view(), name='add_room'),
    path('rooms/', RoomsPageView.as_view(), name='rooms'),
    path('rooms/<slug_room>/true', is_hidden_true, name='true'),
    path('rooms/<slug_room>/false', is_hidden_false, name='false'),
    path('book-applications/', BookApplicationsPageView.as_view(), name='book_applications'),
    path('book-applications/<slug_book_application>/', approve_application, name='application_detail'),
    path('application/<slug_book_application>/change_status/', change_status, name='change_status'),
]
