from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from PIL import Image
import uuid, os


def unique_name(instance, filename):
    ext = os.path.splitext(filename)[1]
    return f"{uuid.uuid4()}{ext}"


class Drawing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    medium = models.CharField(max_length=100, blank=True,
                              help_text="Material or tool used to create the artwork (e.g., Oil on canvas, Procreate, Blender).")
    image = models.ImageField(
        upload_to=unique_name,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(["jpg", "jpeg", "png", "gif", "webp", "avif"])],
        help_text="Allowed formats: JPG, JPEG, PNG, GIF, WebP, AVIF."
    )
    video = models.FileField(
        upload_to=unique_name,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(['mp4', 'mov', 'webm', 'ogv'])],
        help_text="Allowed formats: MP4, MOV, WebM, OGV."
    )
    pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def clean(self):
        super().clean()
        if self.video and not self.image:
            raise ValidationError("An image is required when uploading a video.")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


FONT_CHOICES = [
    ("Andale Mono, monospace", "Andale Mono"),
    ("Arial, sans-serif", "Arial"),
    ("Book Antiqua, Palatino, serif", "Book Antiqua"),
    ("Courier New, monospace", "Courier New"),
    ("Georgia, serif", "Georgia"),
    ("Impact, sans-serif", "Impact"),
    ("Lucida Console, monospace", "Lucida Console"),
    ("Lucida Sans Unicode, sans-serif", "Lucida Sans Unicode"),
    ("Palatino Linotype, Palatino, serif", "Palatino Linotype"),
    ("Segoe UI, sans-serif", "Segoe UI"),
    ("Tahoma, sans-serif", "Tahoma"),
    ("Times New Roman, serif", "Times New Roman"),
    ("Trebuchet MS, sans-serif", "Trebuchet MS"),
    ("Verdana, sans-serif", "Verdana"),
]

def validate_favicon_size(image):
    with Image.open(image) as img:
        if img.size not in [(16, 16), (32, 32)]:
            raise ValidationError("Favicon must be 16×16 or 32×32 pixels.")
    image.seek(0)



class SiteSettings(models.Model):
    header_text = models.CharField(max_length=200, default="Portfolio", verbose_name="Header Text")
    header_bg = models.CharField(max_length=20, default="#343a40", verbose_name="Header Background Color")
    header_text_color = models.CharField(max_length=20, default="#ffffff", verbose_name="Header Text Color")
    site_bg = models.CharField(max_length=20, default="#ffffff", verbose_name="Site Background Color")
    font_family = models.CharField(max_length=100, choices=FONT_CHOICES, default="Arial, sans-serif",
                                   verbose_name="Site Font")
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
    show_media_type = models.BooleanField(default=True, verbose_name="Show Media Type Label")
    show_pinned_label = models.BooleanField(default=True, verbose_name="Show Pinned Label")
    pinned_label_text = models.CharField(max_length=50, default="📌 Pinned", verbose_name="Pinned Label Text")
    pinned_label_text_color = models.CharField(max_length=20, default="#212529", verbose_name="Label Text Color")
    pinned_label_bg = models.CharField(max_length=20, default="#ffc107", verbose_name="Label Background Color")
    show_uploaded_date = models.BooleanField(default=True, verbose_name="Show Uploaded Date")
    uploaded_date_color = models.CharField(max_length=20, default="#6c757d", verbose_name="Uploaded Date Text Color")
    medium_text_color = models.CharField(max_length=20, default="#6c757d", verbose_name="Medium Text Color")
    show_intro = models.BooleanField(default=True, verbose_name="Show Introduction")
    show_download = models.BooleanField(default=True, verbose_name="Show Download Button")
    intro_text = models.TextField(blank=True, default="Welcome to my portfolio!", verbose_name="Introduction Text")
    intro_text_color = models.CharField(max_length=20, default="#000000", verbose_name="Introduction Text Color")
    separator_color = models.CharField(max_length=20, default="#dee2e6", verbose_name="Separator Line Color")
    favicon = models.ImageField(
        upload_to=unique_name,
        blank=True,
        null=True,
        verbose_name="Favicon",
        help_text="Must be 16×16 or 32×32 px. Allowed formats: ICO, PNG, JPG, JPEG, SVG.",
        validators=[
            FileExtensionValidator(['ico', 'png', 'jpg', 'jpeg', 'svg']),
            validate_favicon_size
        ]
    )

    def __str__(self):
        return "Site Settings"

    class Meta:
        verbose_name_plural = "Site Settings"
