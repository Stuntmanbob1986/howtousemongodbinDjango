from django import template
from bson.objectid import ObjectId

register = template.Library()


# @register.simple_tag
@register.filter(name='underscoreTag')
def underscoreTag(obj, attribute):
    print(f'obj:  {obj}, attribute: {attribute}')
    # print(ObjectId(obj))
    obj = dict(obj)
    print(obj.get(attribute))
    return obj.get(attribute)
