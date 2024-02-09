from django.urls import path
from .views import SignUpView, ProfileEditView, DashboardView, PortfolioView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("<slug:slug>/edit/", ProfileEditView.as_view(), name="profile"),
    path("<slug:slug>", PortfolioView.as_view(), name="portfolio" )
]