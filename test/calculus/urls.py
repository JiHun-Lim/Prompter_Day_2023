from allauth.account import views as allauth_views
from django.urls import path

from calculus.views import ProblemListView, AnswerCreateView, AnswerDetailView

urlpatterns = [
    path("accounts/login/", allauth_views.LoginView.as_view(), name="account_login"),
    path("accounts/logout/", allauth_views.LogoutView.as_view(), name="account_logout"),
    path("accounts/signup/", allauth_views.SignupView.as_view(), name="account_signup"),
    path("", ProblemListView.as_view(), name="problem_list"),
    path("<int:pk>/", AnswerDetailView.as_view(), name="answer_detail"),
    path("create/", AnswerCreateView.as_view(), name="answer_create"),
]