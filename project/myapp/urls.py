# from project.myapp.views import post_list
from .views import post_list, RegisterView
from django.urls import path


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    # path("login/", CustomLoginView.as_view(), name="login"),
    # path("logout/", Customsudo rm -f ./.git/index.lockcLogoutView.as_view(), name="logout"),

    path("templates", post_list, name="post_list")
]
