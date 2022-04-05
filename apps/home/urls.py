from django.urls import path
from .views import HomeView, PopulationCreateView, PopulationUpdateView, PopulationDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('pop/create/', PopulationCreateView.as_view(), name='pop_create'),
    path('pop/<int:pk>/', PopulationUpdateView.as_view(), name='pop_update'),
    path('pop/<int:pk>/delete/', PopulationDeleteView.as_view(), name='pop_delete'),
]
