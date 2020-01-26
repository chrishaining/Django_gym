from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('member/new/', views.member_new, name='member_new'),
    path('session/new/', views.session_new, name='session_new'),
    path('instructor/new/', views.instructor_new, name='instructor_new')
]

