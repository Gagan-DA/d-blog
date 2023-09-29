from .models import Category

def catgories(request):
    return { "categories": Category.objects.all() }

def ncatgories(request):
    ncatgories_list=["Sports","Health","World","Business","Nation","Entertainment"]
    return { "ncatgories": ncatgories_list }
