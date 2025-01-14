from datetime import timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from accounts.models import User
from .models import SubscriptionPlan


@login_required
def plan_list(request):
    """نمایش لیست پلن‌ها"""
    plans = SubscriptionPlan.objects.all()
    context = {
        'plans': plans,
        'user_subscription_active': request.user.is_subscription_active(),
        'subscription_end': request.user.subscription_end,
    }
    return render(request, './blog/plan_list.html', context)


@login_required
def buy_plan(request, plan_id):
    """شبیه‌سازی خرید — بدون درگاه واقعی"""
    plan = get_object_or_404(SubscriptionPlan, id=plan_id)
    user = request.user

    # اگر اشتراک فعال دارد، به انتهای آن اضافه کن
    now = timezone.now()
    if user.subscription_end and user.subscription_end > now:
        user.subscription_end = user.subscription_end + timedelta(days=plan.duration_days)
    else:
        user.subscription_start = now
        user.subscription_end = now + timedelta(days=plan.duration_days)

    user.subscription = plan.plan_type
    user.save()

    messages.success(
        request,
        f"اشتراک «{plan.get_plan_type_display()}» با موفقیت فعال شد."
    )
    return redirect('subscriptions:payment_success')


@login_required
def payment_success(request):
    """صفحه نتیجه پرداخت موفق"""
    user = request.user
    context = {
        'subscription_active': user.is_subscription_active(),
        'subscription_type': user.get_subscription_display(),
        'subscription_end': user.subscription_end,
    }
    return render(request, './blog/payment_success.html', context)