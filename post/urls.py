from django.urls import path
from .views import PostListView


urlpatterns = [
    
    path('list', PostListView.as_view(), name="post-list" ),
    path('postnum/<int:id>', PostListView.as_view(), name="post-list" ),
    
]