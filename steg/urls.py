from django.urls import path, include
from steg import views

APP_NAME='steg'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('edit/<int:id>', views.edit_blog, name='edit'),
    path('delete/<int:id>', views.del_blog, name='delete'),
    path('view/<int:id>', views.view_blog, name='view'),
    path('search/<str:key>', views.search_blog, name='view'),
    path('login', views.login_users, name='login')
]
