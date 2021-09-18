from django.urls import path
from .views import CookieStandList, CookieStandDetails

urlpatterns = [
    path('', CookieStandList.as_view(), name='cookie_stand_list'),
    path('<int:pk>/', CookieStandDetails.as_view(), name='cookie_stand_details'),
]