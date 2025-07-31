from django.db import models
from django.core.validators import FileExtensionValidator
import uuid, os


def unique_name(filename):
    ext = os.path.splitext(filename)[1]
    return f"{uuid.uuid4()}{ext}"


def drawing_upload_path(instance, filename):
    return f"drawings/{unique_name(filename)}"


def favicon_upload_path(instance, filename):
    return f"favicons/{unique_name(filename)}"


class Drawing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=drawing_upload_path)
    pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class SiteSettings(models.Model):
    header_text = models.CharField(max_length=200, default="Portfolio", verbose_name="Header Text")
    header_bg = models.CharField(max_length=20, default="#343a40", verbose_name="Header Background Color")
    header_text_color = models.CharField(max_length=20, default="#ffffff", verbose_name="Header Text Color")
    site_bg = models.CharField(max_length=20, default="#ffffff", verbose_name="Site Background Color")
    card_bg = models.CharField(max_length=20, default="#ffffff", verbose_name="Card Background Color")
    card_border_color = models.CharField(max_length=20, default="#dee2e6", verbose_name="Card Border Color")
    card_text_color = models.CharField(max_length=20, default="#000000", verbose_name="Card Text Color")
    footer_bg = models.CharField(max_length=20, default="#f8f9fa", verbose_name="Footer Background Color")
    footer_text = models.TextField(
        default="© All rights reserved. The content displayed on this site are the intellectual property of the website owner. Unauthorized use, redistribution, or reproduction of any material without explicit permission is strictly prohibited.",
        verbose_name="Footer Text")
    footer_text_color = models.CharField(max_length=20, default="#000000", verbose_name="Footer Text Color")
    owner_name = models.CharField(max_length=100, blank=True, verbose_name="Owner Name")
    owner_email = models.EmailField(blank=True, verbose_name="Owner Email")
    button_bg = models.CharField(max_length=20, default="#6c757d", verbose_name="Button Background Color")
    button_text_color = models.CharField(max_length=20, default="#ffffff", verbose_name="Button Text Color")
    button_text = models.CharField(max_length=100, default="← Back to portfolio", verbose_name="Button Text")
    pinned_label_text = models.CharField(max_length=50, default="📌 Pinned", verbose_name="Pinned Label Text")
    pinned_label_text_color = models.CharField(max_length=20, default="#212529", verbose_name="Pinned Label Text Color")
    pinned_label_bg = models.CharField(max_length=20, default="#ffc107", verbose_name="Pinned Label Background")
    show_uploaded_date = models.BooleanField(default=True, verbose_name="Show Uploaded Date")
    uploaded_date_color = models.CharField(max_length=20, default="#6c757d", verbose_name="Uploaded Date Text Color")
    show_intro = models.BooleanField(default=True, verbose_name="Show Introduction")
    show_download = models.BooleanField(default=True, verbose_name="Show Download Button")
    intro_text = models.TextField(blank=True, default="Welcome to my portfolio!", verbose_name="Introduction Text")
    intro_text_color = models.CharField(max_length=20, default="#000000", verbose_name="Introduction Text Color")
    separator_color = models.CharField(max_length=20, default="#dee2e6", verbose_name="Separator Line Color")
    favicon = models.ImageField(upload_to=favicon_upload_path, blank=True, null=True,
                                verbose_name="Favicon (32x32 .ico/.png/.jpg)",
                                validators=[FileExtensionValidator(['ico', 'png', 'jpg', 'jpeg'])])

    def __str__(self):
        return "Site Settings"

    class Meta:
        verbose_name_plural = "Site Settings"
