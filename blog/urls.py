from django.urls import path
from .import views

urlpatterns = [
    path('', views.HomeView.as_view(),name="home"),
    path('home/', views.HomeView.as_view(),name="home"),
    path('article/<int:pk>', views.ArticleView.as_view(),name="article"),
    path('addpost/', views.AddPostView.as_view(),name="addpost"),
    path('updatepost/<int:pk>', views.UpdatePostView.as_view(),name="updatepost"),
    path('deletepost/<int:pk>', views.DeletePostView.as_view(),name="deletepost"),
    path('category/<str:cname>', views.CategoryView,name="category"),
    path('like_post/<int:pk>', views.likeView,name="like_post"),
    path('comment', views.MyFormView.as_view(), name='comment'),


]
