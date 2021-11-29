from django.urls import path

from app1 import views

app_name = 'app1'

urlpatterns = [
    path('', views.CreateLocationView.as_view(), name='add'),
    path('<int:pk>/update/', views.UpdateLocationView.as_view(), name='modify'),
    path('list/', views.ListLocationView.as_view(), name='listare')
]