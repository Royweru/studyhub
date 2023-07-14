from django.urls import path
from. import views

urlpatterns = [
    path('',views.room_page , name='rooms'),
    # path('<str:pk>/', views.getroom, name='room'),
    path('create-room/',views.create_room, name='create')
]
