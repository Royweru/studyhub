from django.urls import path
from. import views
urlpatterns = [
    path('',views.room_page),
    path('<str:pk>/', views.getroom)
]
