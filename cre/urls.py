from django.urls import path
from .views import home_view, components_view

urlpatterns = [
    path('', home_view, name="home-page"),
    path('components/', components_view, name="components-page"),
]
