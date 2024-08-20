from django.db.models import Prefetch
from django import template
from menu.models import Menu, MenuItem

register = template.Library()

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_slug):
    try:
        menu = Menu.objects.prefetch_related(
            Prefetch(
                'items',
                queryset=MenuItem.objects.select_related('parent')
            )
        ).get(slug=menu_slug)

        active_url = context['request'].path

        items = list(menu.items.all())

        def build_tree(parent):
            tree = []
            for item in items:
                if item.parent == parent:
                    children = build_tree(item)
                    tree.append({
                        'item': item,
                        'children': children,
                        'active': active_url.startswith(item.get_absolute_url())
                    })
            return tree

        return {'menu_tree': build_tree(None), 'menu': menu}
    except Menu.DoesNotExist:
        return {'menu_tree': [], 'menu': None}
