from django.urls import path, include
from . import views

app_name="blogs"
urlpatterns = [
    path('', views.index,name='index'),
    # e%: /blogs/5
    path('article',include([
        path('',views.index),
        path('add',views.add),
        path('edit/<int:article_id>',views.edit),
        path('delete/<int:article_id>',views.delete),
    ])),
]
