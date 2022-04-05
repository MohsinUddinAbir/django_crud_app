from django.urls import path
from .views import BlogView, PostView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('<pk>/<slug:slug>/', PostView.as_view(), name='post_details'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
