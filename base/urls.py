from django.urls import path,include
from .views import PostList,PostDetail
urlpatterns = [
    path('',PostList.as_view(), name='list'),
    path('detail/<int:pk>/',PostDetail.as_view(), name='detail'),

]