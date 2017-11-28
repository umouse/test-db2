from django import template

from blog.models import Like

register = template.Library()

@register.simple_tag
def is_liked(post,user):
   return Like.objects.filter(post=post, user=user).count()