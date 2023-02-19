from django.urls import path
from .views import RegisterView, RetrieveUserView

# Our API endpoint extentions for user base protocols
urlpatterns = [
    path('register', RegisterView.as_view()),
    path('user', RetrieveUserView.as_view())
]