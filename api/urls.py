from .views import user, user_detail, category, category_detail, create, create_detail
from django.urls import path

urlpatterns = [
    path('user/', user),
    path('user/<int:pk>/', user_detail),
    path('category/',category),
    path('category/<int:pk>/', category_detail),
    path('create/', create),
    path('create/<int:pk>/', create_detail),
]
