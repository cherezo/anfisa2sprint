from django.shortcuts import render
from ice_cream.models import IceCream
from django.db.models import Q


#def index(request):
#   template = 'homepage/index.html'
#    return render(request, template)

def index(request):
    template = 'homepage/index.html'
    # Запишите в переменную ice_cream_list новый QuerySet
     # Запрашиваем нужные поля из базы данных:
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'price', 'description'
    ).filter(
        # Проверяем, что
        is_published=True,  # Сорт разрешён к публикации;
        is_on_main=True,  # Сорт разрешён к публикации на главной странице;
        category__is_published=True  # Категория разрешена к публикации.
    )
    # Делаем запрос, объединяя два условия
        # через Q-объекты и оператор AND:
    #    Q(is_published=True) & (Q(is_on_main=True) | Q(description__contains='икра'))).order_by('title')[:3]
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)
