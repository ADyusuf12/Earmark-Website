from django.apps import AppConfig
from django.db.models.signals import post_migrate

def create_groups(sender, **kwargs):
    # Import models here to avoid "Apps aren't loaded yet" error
    from django.contrib.auth.models import Group, Permission

    # Define groups and their permissions
    group_permissions = {
        'Customer': [],
        'Real Estate Agent': ['add_properties_listing', 'change_properties_listing', 'delete_properties_listing'],
        'Real Estate Company': ['add_properties_listing', 'change_properties_listing', 'delete_properties_listing'],
        'Property Developer': ['add_properties_listing', 'change_properties_listing', 'delete_properties_listing'],
        'Property Owner': ['add_properties_listing', 'change_properties_listing', 'delete_properties_listing'],
    }

    for group_name, permissions in group_permissions.items():
        group, _ = Group.objects.get_or_create(name=group_name)  # Create group if it doesn't exist

        for permission_codename in permissions:
            permission = Permission.objects.get(codename=permission_codename)  # Fetch permission
            group.permissions.add(permission)


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'e_web.apps.accounts'

    def ready(self):
        # Import signals here to avoid "Apps aren't loaded yet" error
        import e_web.apps.accounts.signals

        # Connect the post_migrate signal for group creation
        post_migrate.connect(create_groups, sender=self)
