from django.contrib import admin
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.html import mark_safe
from .models import Drawing, SiteSettings

@admin.register(Drawing)
class DrawingAdmin(admin.ModelAdmin):
    list_display = ('title', 'pinned', 'created_at')
    list_filter = ('pinned', 'created_at')
    search_fields = ('title',)

    readonly_fields = ("drawing_preview",)

    def drawing_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="300" style="border:1px solid #ccc; margin-top:10px;" />')
        return "No image uploaded yet."

    drawing_preview.short_description = "Preview"

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("🧢 Header Settings", {
            "fields": ("header_text", "header_text_color", "header_bg")
        }),
        ("🌐 Site Background and Favicon", {
            "fields": ("site_bg", "favicon")
        }),
        ("📄 Introduction Section", {
            "fields": ("show_intro", "intro_text", "intro_text_color", "separator_color")
        }),
        ("🖼️ Card Styling", {
            "fields": ("card_bg", "card_text_color", "card_border_color", "pinned_label_text", "pinned_label_text_color", "pinned_label_bg")
        }),
        ("📌 Post Details", {
            "fields": ("show_uploaded_date", "uploaded_date_color", "button_text", "button_text_color", "button_bg", "show_download")
        }),
        ("📭 Footer", {
            "fields": ("footer_text", "owner_name", "owner_email", "footer_text_color", "footer_bg")
        }),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        settings = SiteSettings.objects.first()
        if settings:
            return HttpResponseRedirect(reverse('admin:drawings_sitesettings_change', args=[settings.id]))
        return super().changelist_view(request, extra_context=extra_context)