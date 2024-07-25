# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('myapi/google-login/', views.google_login, name='google_login'),
    path('myapi/districts/<str:state_name>/', views.GetDistrictsView.as_view(), name='get_districts'),
    path('myapi/colleges/<str:state_name>/<str:district_name>/', views.GetCollegesView.as_view(), name='get_colleges'),
    path('myapi/submit-form/', views.SubmitFormView.as_view(), name='submit_form'),
]
