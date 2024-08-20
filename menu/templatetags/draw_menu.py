from django import template
from menu.models import Menu, MenuItem

register = template.Library()

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_slug):
    try:
        menu = Menu.objects.get(slug=menu_slug)
        items = MenuItem.objects.filter(menu=menu).select_related('parent').prefetch_related('children')
        active_url = context['request'].path

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
