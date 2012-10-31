from django import template
from django.template import Context, Template
from django.template.loader import render_to_string

from django.conf import settings

register = template.Library()


@register.simple_tag(takes_context=True)
def idl_popup(context, variant):
    """Return javascript for the main Internet Defense League popup/banner"""

    t = ''
    if getattr(settings, 'DEFENSE_LEAGUE', False):
        t = render_to_string('internetdefenseleague/defenseleague.html', {'variant': variant})
    return t

@register.simple_tag()
def idl_super_badge():
    """Display the Internet Defense League super badge"""
    t = ''
    if getattr(settings, 'DEFENSE_LEAGUE', False):
        t = render_to_string('internetdefenseleague/super_badge.html')

    return t

@register.simple_tag()
def idl_shield_badge():
    """Display the Internet Defense League shield badge"""
    t = ''
    if getattr(settings, 'DEFENSE_LEAGUE', False):
        t = render_to_string('internetdefenseleague/shield_badge.html')

    return t

@register.simple_tag()
def idl_sidebar_badge():
    """Display the Internet Defense League sidebar badge"""
    t = ''
    if getattr(settings, 'DEFENSE_LEAGUE', False):
        t = render_to_string('internetdefenseleague/sidebar_badge.html')

    return t

@register.simple_tag()
def idl_footer_badge():
    """Display the Internet Defense League footer badge"""
    t = ''
    if getattr(settings, 'DEFENSE_LEAGUE', False):
        t = render_to_string('internetdefenseleague/footer_badge.html')

    return t

@register.simple_tag()
def idl_left_ribbon():
    """Display the Internet Defense League left ribbon badge"""
    t = ''
    if getattr(settings, 'DEFENSE_LEAGUE', False):
        t = render_to_string('internetdefenseleague/ribbon_left.html')

    return t

@register.simple_tag()
def idl_right_ribbon():
    """Display the Internet Defense League right ribbon badge"""
    t = ''
    if getattr(settings, 'DEFENSE_LEAGUE', False):
        t = render_to_string('internetdefenseleague/ribbon_right.html')

    return t
