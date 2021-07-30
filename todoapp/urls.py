from django.urls import path
from django.urls.resolvers import URLPattern

from .views import *

urlpatterns=[
    path('', home, name='home'),
    path('createitem/', ItemCreate.as_view(), name='create'),
    path('viewitem/', ItemView.as_view(), name='view'),
    path('viewitem/<int:my_item>/', ItemDetail.as_view(), name='detail'),
    path('viewitem/<int:my_item>/updateitem/', ItemUpdate.as_view(), name='update'),
        path('viewitem/<int:my_item>/deleteitem/', ItemDelete.as_view(), name='delete'),
]