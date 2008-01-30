from django.template import Library

register = Library()

@register.inclusion_tag('points.html')
def load_positions(cl):
    """
    Returns xxx
    """
    return {'points':cl.model.objects.all()}
