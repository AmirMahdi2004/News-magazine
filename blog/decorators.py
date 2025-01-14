from functools import wraps

from django.contrib import messages
from django.shortcuts import redirect


def subscription_required(view_func):
    """
    فقط کاربرانی که اشتراک فعال دارند می‌توانند ویو را ببینند.
    اگر لاگین نکرده باشد → به login
    اگر لاگین کرده ولی اشتراک ندارد → به صفحه خرید اشتراک
    """
    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        # اگر لاگین نکرده
        if not request.user.is_authenticated:
            return redirect('accounts:login')

        # اگر اشتراک فعال ندارد
        if not request.user.is_subscription_active():
            messages.warning(
                request,
                "برای مشاهده این بخش باید اشتراک فعال داشته باشید."
            )
            return redirect('subscriptions:plan_list')

        return view_func(request, *args, **kwargs)

    return _wrapped