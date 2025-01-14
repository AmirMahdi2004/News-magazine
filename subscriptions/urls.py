from django.urls import path
from . import views

app_name = 'subscriptions'

urlpatterns = [
    path('plans/', views.plan_list, name='plan_list'),
    path('buy/<int:plan_id>/', views.buy_plan, name='buy_plan'),
    path('success/', views.payment_success, name='payment_success'),
]