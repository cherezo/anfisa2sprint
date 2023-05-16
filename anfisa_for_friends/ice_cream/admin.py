from django.contrib import admin

# Из модуля models импортируем модели...
from .models import Category
from .models import Topping
from .models import Wrapper
from .models import IceCream

# Для перечисленных импортированных моделей:
# В случае пустого поля вместо прочерка выводить "Не задано"
admin.site.empty_value_display = 'Не задано'




# Создаём собственный класс IceCreamAdmin, в котором будем описывать настройки админки:
# наследуем его от стандартного класса admin.ModelAdmin
class IceCreamAdmin(admin.ModelAdmin):
    # В этом классе опишем все настройки, какие захотим.
    
    # какие поля будут показаны на странице списка объектов (свойство list_display (это кортеж));
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )

    # какие поля можно редактировать прямо на странице списка объектов (свойство list_editable, кортеж);
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )

    # search_fields — кортеж с перечнем полей, по которым будет проводиться поиск. 
    # Форма поиска отображается над списком элементов.
    search_fields = ('title',) 

    # list_filter — кортеж с полями, по которым можно фильтровать записи. 
    # Фильтры отобразятся справа от списка элементов.
    list_filter = ('category',)

    # В кортеже list_display_links указывают поля, при клике на которые можно перейти на страницу просмотра и редактирования записи. 
    # По умолчанию такой ссылкой служит первое отображаемое поле.
    list_display_links = ('title',)

    # Модели IceCream и Topping связаны как «многие ко многим».
    # изменим интерфейс так, чтобы связанные записи можно было перекладывать из одного окошка в другое.
    filter_horizontal = ('toppings',)


# Подготавливаем модель IceCream для вставки на страницу другой модели.
class IceCreamInline(admin.TabularInline):
    model = IceCream
    # Переменная extra указвает сколько не заполненых полей добавить на страницу
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',        
    )


# Регистрируем класс IceCream с собственными настройками админки: 
# указываем, что для отображения админки модели IceCream
# вместо стандартного класса нужно нужно использовать класс IceCreamAdmin 
admin.site.register(IceCream, IceCreamAdmin)

# Регистрируем модели в админке:
admin.site.register(Category, CategoryAdmin)
admin.site.register(Topping)
admin.site.register(Wrapper)