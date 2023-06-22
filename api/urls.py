from django.urls import path
from api import apis

APP_NAME='api'

urlpatterns = [
    path('', apis.blood_doner, name='api_home'),
    path('test/', apis.index, name='test'),
    path('view/<int:id>', apis.view_doner, name='view_doner')
]