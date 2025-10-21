from .models import Brand, Mobile
from django.db.models import Q, F

def all_brands_not_in_korea_china():

    query = Brand.objects.filter(~Q(nationality='China')
    & ~Q(nationality='Korea'))
 
  
    return query

def some_brand_mobiles(*brand_names):

    query = Mobile.objects.filter(brand__name__in=brand_names)
    all_mobiles = Mobile.objects.all()
    

    if not query.exists():
        return all_mobiles
    else:
        return query

def mobiles_brand_nation_equals_made_in():

    query = Mobile.objects.filter(made_in=F('brand__nationality'))
    return query
