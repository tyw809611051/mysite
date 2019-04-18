from django.urls import path
from . import views

app_name="blogs"
urlpatterns = [
    path('', views.index,name='index'),
    # e%: /blogs/5
    path('article/<int:article_id>/', views.detail, name='detail'),
    path('article/add', views.add, name='add'),
]
