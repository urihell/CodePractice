from django.urls import path

from . import views

app_name = 'crm'
urlpatterns = [
    path('', views.index, name='index'),
    path('organizations/<int:organization_id>/', views.organization, name='organization'),
    path('organizations/', views.organization, name='organization'),
    path('customers/<int:customer_id>/', views.customer, name='customer')
]

