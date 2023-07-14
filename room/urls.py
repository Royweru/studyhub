from django.urls import path
from. import views

urlpatterns = [
    path('room/',views.room_page , name='rooms'),
    path('room/<str:pk>/', views.get_room, name='room'),

    path('create-room/',views.create_room, name='create')
]
