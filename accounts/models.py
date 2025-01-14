from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    class SubscriptionType(models.TextChoices):
        FREE = 'free', 'Free'
        MONTHLY = 'monthly', 'Monthly'
        YEARLY = 'yearly', 'Yearly'

    class UserRole(models.TextChoices):
        READER = 'reader', 'Reader'
        AUTHOR = 'author', 'Author'
        EDITOR = 'editor', 'Editor'

    email = models.EmailField(
        unique=True,
        verbose_name='Email'
    )

    first_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='First name'
    )

    last_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Last name'
    )

    avatar = models.ImageField(
        upload_to='users/avatars/',
        blank=True,
        null=True,
        verbose_name='Avatar'
    )

    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.READER
    )

    subscription = models.CharField(
        max_length=20,
        choices=SubscriptionType.choices,
        default=SubscriptionType.FREE
    )

    subscription_start = models.DateTimeField(
        blank=True,
        null=True
    )

    subscription_end = models.DateTimeField(
        blank=True,
        null=True
    )

    def is_subscription_active(self):
        if self.subscription == self.SubscriptionType.FREE:
            return False

        if not self.subscription_end:
            return False

        return self.subscription_end > timezone.now()

    def __str__(self):
        return self.username