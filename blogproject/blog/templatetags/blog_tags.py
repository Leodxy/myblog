from .. import models
from django import template
from django.db.models.aggregates import Count
from django.shortcuts import render,redirect,get_object_or_404
register=template.Library()
# 最新文章模板标签
@register.simple_tag
def get_recent_posts(num=5):
    return models.Post.objects.all()[:num]
    # return models.Post.objects.all().order_by('-created_time')[:num]
# 归档模板标签
@register.simple_tag
def archives():
    return models.Post.objects.dates('created_time', 'month', order='DESC')
    # return models.Post.objects.dates('created_time','month',order='DESC')

# 分类模板标签
@register.simple_tag
def get_categories():
    return models.Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0) # post是关联的数据库模型(小写)
    # return models.Category.objects.all()
# register.filter("get_recenst_posts",get_recenst_posts)  # 1 注册为模板标签 或者使用装饰器

# 标签云
@register.simple_tag
def get_tags():
    return models.Tag.objects.annotate(num_tags=Count('post')).filter(num_tags__gte=1)
