from django.urls import path
from .views import Myview

urlpatterns = [
    path('', Myview.as_view(), name='myview')
]
