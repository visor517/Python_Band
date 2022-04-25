# TODO разобраться можно ли наследовать существующий контекстный процессор для работы с меню.
from articleapp.models import Category


def menu_category_context(request):

    categories = Category.objects.all()

    return {
        'categories': categories
        }


