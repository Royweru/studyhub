from django.urls import path
from. import views

urlpatterns = [
    path('login/' , views.LoginPage, name='login'),

    path('room/',views.room_page , name='rooms'),
    path('room/<str:pk>/', views.get_room, name='room'),

    path('create-room/',views.create_room, name='create'),
    path('update-room/<str:pk>/',views.update_room, name='update'),
    path('delete-room/<str:pk>/',views.deleteRoom, name='delete' )
]
