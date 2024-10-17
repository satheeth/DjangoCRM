from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserRegistrationView, AddRecord, GetRecord, DeleteRecord, UpdateRecord, DetailedRecord

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
    path("register/", UserRegistrationView.as_view(), name = "user_registeration"),
    path("getRecords/", GetRecord.as_view()),
    path("addRecord/", AddRecord.as_view()),
    path("deleteRecord/<int:id>", DeleteRecord.as_view()),
    path("updateRecord/<int:id>", UpdateRecord.as_view()),
    path("detailedRecord/<int:id>", DetailedRecord.as_view())
]
