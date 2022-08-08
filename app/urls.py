from django.urls import path
from app.views import Register,Login,Logout,Payment
urlpatterns = [
    path('register/',Register.as_view()),
    path('login/',Login.as_view()),
    path('logout/',Logout.as_view()),
    path('payment/',Payment.as_view()),
    #path('details/',PersonalInfo.as_view()),
]
