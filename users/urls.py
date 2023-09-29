
from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(),name="register"),
    path('signin/', views.CustomLoginView.as_view(),name="signin"),
    path('editprofile/',views.UserEditView.as_view(),name="editprofile"),
    path('password/',views.PasswordsChangeView.as_view(),name="password"),
    path('passwordsuccess/',views.PasswordsuccessView,name="passwordsuccess"),
    path('userprofile/<int:pk>',views.ShowProfilePage.as_view(),name="userprofile"),
    path('editprofileinfo/<int:pk>',views.EditProfileView.as_view(),name="editprofileinfo"),
    path('createprofileinfo',views.CreateProfileView.as_view(),name="createprofileinfo"),

]
