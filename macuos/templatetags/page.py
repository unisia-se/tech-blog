from django import template
 
register = template.Library()
 
@register.simple_tag
def url_replace(request, value):
    dict_ = request.GET.copy()
    dict_["page"] = value
    return dict_.urlencode()
