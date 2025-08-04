import os
from django.db.models.signals import post_delete, pre_save, post_migrate
from django.dispatch import receiver
from .models import Drawing, SiteSettings
from .context_processors import defaults

DEBUG = os.environ.get("DEBUG", "False").lower() in ("true", "1")


@receiver(post_delete, sender=Drawing)
def delete_media(sender, instance, **kwargs):
    if instance.image:
        if DEBUG and os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
        else:
            instance.image.delete(save=False)
    if instance.video:
        if DEBUG and os.path.isfile(instance.video.path):
            os.remove(instance.video.path)
        else:
            instance.video.delete(save=False)


@receiver(pre_save, sender=SiteSettings)
def replace_old_favicon(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old = SiteSettings.objects.get(pk=instance.pk)
    except SiteSettings.DoesNotExist:
        return

    if old.favicon and old.favicon != instance.favicon:
        if DEBUG and os.path.isfile(old.favicon.path):
            os.remove(old.favicon.path)
        else:
            old.favicon.delete(save=False)


@receiver(post_migrate)
def create_default_site_settings(sender, **kwargs):
    if not SiteSettings.objects.exists():
        SiteSettings.objects.create(**defaults)
