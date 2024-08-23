from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(
            user=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
            username=instance.username
            )

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
@receiver(post_save, sender=User)
def assign_group_permissions(sender, instance, created, **kwargs):
    if created:
        # Get the group from the user's groups
        group = instance.groups.first()
        if group:
            # Assign group permissions to the user
            for perm in group.permissions.all():
                instance.user_permissions.add(perm)



