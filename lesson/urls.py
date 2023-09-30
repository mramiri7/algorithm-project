from django.urls import path

from . import views

urlpatterns = [
    path('lessons/', views.get_lessons),
    path('lessons/<int:lesson_id>/', views.get_lesson),
]
