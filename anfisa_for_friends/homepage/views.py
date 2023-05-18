from django.shortcuts import render
from ice_cream.models import IceCream
from django.db.models import Q


#def index(request):
#   template = 'homepage/index.html'
#    return render(request, template)

def index(request):
    template = 'homepage/index.html'
    # Запишите в переменную ice_cream_list новый QuerySet
    ice_cream_list = IceCream.objects.values('id', 'title', 'description'
    # Верни только те объекты, у которых в поле is_on_main указано True:
        ).filter(# Делаем запрос, объединяя два условия
        # через Q-объекты и оператор AND:
        Q(is_published=True) & (Q(is_on_main=True) | Q(description__contains='икра')))
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)
