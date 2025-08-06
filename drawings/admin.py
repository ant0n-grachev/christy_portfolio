from django.contrib import admin
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.html import mark_safe
from .models import Drawing, SiteSettings


class DrawingAdminForm(forms.ModelForm):
    media_type = forms.ChoiceField(
        choices=(('image', 'Image'), ('video', 'Video')),
        required=False,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Drawing
        fields = ['title', 'description', 'medium', 'pinned', 'media_type', 'image', 'video']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False
        self.fields['video'].required = False
        if self.instance.pk:
            if self.instance.video:
                self.fields['media_type'].initial = 'video'
            elif self.instance.image:
                self.fields['media_type'].initial = 'image'

    def clean(self):
        cleaned = super().clean()
        media_type = cleaned.get('media_type')
        image = cleaned.get('image')
        video = cleaned.get('video')
        if media_type == 'image':
            if not image:
                raise forms.ValidationError('Please upload an image.')
            cleaned['video'] = None
        elif media_type == 'video':
            if not video:
                raise forms.ValidationError('Please upload a video.')
            if not image:
                raise forms.ValidationError('Please upload an image to use as the video cover.')
        else:
            raise forms.ValidationError('Select a media type.')
        return cleaned


@admin.register(Drawing)
class DrawingAdmin(admin.ModelAdmin):
    form = DrawingAdminForm
    list_display = ('title', 'pinned', 'created_at')
    list_filter = ('pinned', 'created_at')
    search_fields = ('title',)

    readonly_fields = ("drawing_preview",)
    fields = ('title', 'description', 'medium', 'pinned', 'media_type', 'image', 'video', 'drawing_preview')

    def drawing_preview(self, obj):
        if obj.video:
            poster = f' poster="{obj.image.url}"' if obj.image else ''
            return mark_safe(
                f'<video src="{obj.video.url}" width="300" controls{poster} style="border:1px solid #ccc; margin-top:10px;"></video>'
            )
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width="300" style="border:1px solid #ccc; margin-top:10px;" />'
            )
        return "No media uploaded yet."

    drawing_preview.short_description = "Preview"

    class Media:
        js = ("drawings/js/media_toggle.js",)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("🧢 Header Settings", {
            "fields": ("header_text", "header_text_color", "header_bg", "favicon")
        }),
        ("🌐 Site Background and Fonts", {
            "fields": ("site_bg", "font_family")
        }),
        ("📄 Introduction Section", {
            "fields": ("show_intro", "intro_text", "intro_text_color", "separator_color")
        }),
        ("🖼️ Card Styling", {
            "fields": ("card_bg", "card_text_color", "card_border_color", "show_media_type", "show_pinned_label",
                       "pinned_label_text", "pinned_label_text_color", "pinned_label_bg")
        }),
        ("📌 Post Details", {
            "fields": ("show_uploaded_date", "uploaded_date_color", "medium_text_color", "button_text",
                       "button_text_color", "button_bg", "show_download")
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
