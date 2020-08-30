from django.urls import path
from . import views
app_name = 'myapp'
urlpatterns = [
    path('',views.home,name="home"),
    path('<int:pk>/delete',views.aliasDelete,name="aliasDelete"),
    path('<int:pk>/update',views.urlUpdate,name="urlUpdate"),
    path('<str:alias>/',views.url_redirect,name="url_redirect"),
    
]