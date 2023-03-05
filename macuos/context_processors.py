
from.models import BigCategory, Tag
 
 
def common(request):
    context = {
        "big_categories": BigCategory.objects.all(),
        "tags": Tag.objects.all(),
    }
    return context
