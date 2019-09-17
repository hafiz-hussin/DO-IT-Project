from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
"""Profile"""
class ProfileQuerySet(models.QuerySet):
    def registered(self):
        return self

    def search(self, query):
        lookup = (
            Q(nric_no__icontains=query),
            Q(name__icontains=query)
        )

        return self.filter(lookup)

class ProfileManager(models.Manager):
    def get_queryset(self):
        return ProfileQuerySet(self.model, using=self._db)

    def registered(self):
        return self.get_queryset().registered()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().registered().search(query)


class profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120, default='last')
    street = models.CharField(max_length=120, default='street')
    city = models.CharField(max_length=120, default='city')
    state = models.CharField(max_length=120, default='state')
    accumulatedMoney = models.DecimalField(max_digits=10 ,decimal_places= 2, default=0.00)

    objects = ProfileManager()

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         profile.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()


    def __unicode__(self):
        return self.firstName


"""History"""
class HistoryQuerySet(models.QuerySet):
    def registered(self):
        return self

    def search(self, query):
        lookup = (
            Q(nric_no__icontains=query),
            Q(name__icontains=query)
        )

        return self.filter(lookup)

class HistoryManager(models.Manager):
    def get_queryset(self):
        return HistoryQuerySet(self.model, using=self._db)

    def registered(self):
        return self.get_queryset().registered()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().registered().search(query)


class History(models.Model):
    qtype = models.CharField(max_length=10, null=False, blank=False)
    person = models.ForeignKey(profile, null=True, on_delete=models.SET_NULL)
    reward = models.DecimalField(max_digits=10 ,decimal_places= 2, default=0.00)
    created_date = models.DateTimeField(auto_now_add=True)

    objects = HistoryManager()

    class Meta:
        ordering = ['-created_date']
        verbose_name_plural = "Histories"

    def __unicode__(self):
        return self.qtype