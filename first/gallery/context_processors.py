from .models import SiteTheme, Category, Artist


def global_context(request):
    return {
        'active_theme': SiteTheme.get_active(),
        'categories':   Category.objects.all(),
        'artist':       Artist.objects.first(),
    }
