from django import template

register = template.Library()

@register.filter
def add_class(field, css_class):
    """ Añade una clase CSS al campo del formulario """
    return field.as_widget(attrs={'class': css_class})
