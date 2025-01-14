from django.contrib import admin
from .models import SubscriptionPlan

# Register your models here.
@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ('plan_type', 'price', 'duration_days')