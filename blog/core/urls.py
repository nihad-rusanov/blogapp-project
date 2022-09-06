from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('home/addBlog/',views.addBlog,name="addBlog"),
    path('home/updateBlog/<str:pk>',views.updateBlog,name="updateBlog"),
    path('home/deleteBlog/<str:pk>',views.deleteBlog,name="deleteBlog")
]