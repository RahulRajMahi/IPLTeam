from django.urls import path
from iplapp import views

urlpatterns = [
    path('', views.home_view, name = 'home'),
    path('add/', views.add_team_view, name = 'add'),
    path('display/', views.display_team_view, name = 'display'),
    path('update/<int:id>', views.update_team_view, name = 'update'),
    path('delete/<int:id>', views.delete_team_view, name = 'delete'),
    
]
