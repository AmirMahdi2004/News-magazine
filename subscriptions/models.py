from django.db import models


class SubscriptionPlan(models.Model):
    class PlanType(models.TextChoices):
        MONTHLY = 'monthly', 'یک ماهه'
        YEARLY = 'yearly', 'یک ساله'

    plan_type = models.CharField(
        max_length=20,
        choices=PlanType.choices,
        unique=True,
        verbose_name="نوع پلن"
    )
    price = models.PositiveIntegerField(verbose_name="قیمت (تومان)")
    duration_days = models.PositiveIntegerField(verbose_name="مدت اعتبار (روز)")

    class Meta:
        verbose_name = "پلن اشتراک"
        verbose_name_plural = "پلن‌های اشتراک"

    def __str__(self):
        return self.get_plan_type_display()