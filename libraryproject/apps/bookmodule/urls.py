from django.urls import path
from . import views

#task6:
urlpatterns = [
    path('', views.index), 
    path('index2/<int:val1>/', views.index2),
    path('<int:bookId>', views.viewbook),#task7
]

