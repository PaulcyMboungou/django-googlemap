from django.template import Library

register = Library()

def gmap_secret_key():
    """
    Returns the string contained in the setting SECRET_KEY.
    """
    try:
        from django.conf import settings
    except ImportError:
        return ''
    return settings.GMAP_SECRET_KEY
gmap_secret_key = register.simple_tag(gmap_secret_key)
