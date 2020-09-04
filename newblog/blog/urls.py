from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.list_view, name="listview"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.detail_view, name="detail_view" ),
]



