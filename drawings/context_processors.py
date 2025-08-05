from .models import SiteSettings

defaults = {
    'header_text': "Portfolio",
    'header_bg': "#343a40",
    'header_text_color': "#ffffff",
    'site_bg': "#ffffff",
    'card_bg': "#ffffff",
    'card_border_color': "#dee2e6",
    'card_text_color': "#000000",
    'footer_bg': "#f8f9fa",
    'footer_text': "© All rights reserved. The content displayed on this website are the intellectual property of the website owner. Unauthorized use, redistribution, or reproduction of any material without explicit permission is strictly prohibited.",
    'footer_text_color': "#000000",
    'owner_name': "",
    'owner_email': "",
    'button_bg': "#6c757d",
    'button_text_color': "#ffffff",
    'button_text': "← Back to portfolio",
    'show_media_type': True,
    'show_pinned_label': True,
    'pinned_label_text': "📌 Pinned",
    'pinned_label_text_color': "#212529",
    'pinned_label_bg': "#ffc107",
    'show_uploaded_date': True,
    'uploaded_date_color': "#6c757d",
    'show_intro': True,
    'show_download': True,
    'intro_text': "Welcome to my portfolio!",
    'intro_text_color': "#000000",
    'separator_color': "#dee2e6",
    'favicon': None,
}


def site_settings(request):
    try:
        settings, created = SiteSettings.objects.get_or_create(defaults=defaults)
        return {'site_settings': settings}
    except:
        return {'site_settings': SiteSettings(**defaults)}
