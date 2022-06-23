from django.urls import path
from .views import TodoAppCreateView

urlpatterns = [
    path('', TodoAppCreateView.as_view()),
#     path('', include('home.html')),
]