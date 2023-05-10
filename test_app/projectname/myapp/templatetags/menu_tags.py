from django import template
from django.utils.html import mark_safe

register = template.Library()

@register.simple_tag
def show_menu_items(menu_items):
    def create_menu_tree(items, parent=None):
        menu = ''
        for item in items:
            if item.parent == parent:
                if item.children.all():  # Используем 'children' вместо 'menuitem_set'
                    menu += '<li class="nav-item dropdown">'
                    menu += '<a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">'
                    menu += item.name
                    menu += '</a>'
                    menu += '<div class="dropdown-menu" aria-labelledby="navbarDropdown">'
                    children = create_menu_tree(items, item)
                    if children:
                        menu += children
                    menu += '</div>'
                else:
                    menu += '<li class="nav-item">'
                    menu += '<a class="nav-link" href="#">{0}</a>'.format(item.name)
                menu += '</li>'
        return menu

    return mark_safe(create_menu_tree(menu_items))  # Оберните итоговую строку в функцию mark_safe
