from django.urls import path
from .views import HomeView,RegistrationView,LoginView,LogoutView,ProfileView,ProfileUpdateView,BlogCreateView,BlogListView,BlogEditView

app_name = 'blogapp'
urlpatterns = [
    # clients
    path('', HomeView.as_view(), name="home"),
    path('registration/', RegistrationView.as_view(), name="registration"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('profileupdate/<int:pk>/', ProfileUpdateView.as_view(), name="profileupdate"),
    path('blogcreate', BlogCreateView.as_view(), name="blogcreate"),
    path('bloglist', BlogListView.as_view(), name="bloglist"),
    path('blogedit/<int:id>/', BlogEditView.as_view(), name="blogedit"),
   
    

]    