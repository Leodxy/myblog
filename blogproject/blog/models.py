from django.db import models
# from django.contrib.auth.models import User
from users.models import User
from django.urls import reverse
from django.utils.html import  strip_tags
import markdown
from collections import defaultdict
#blog/models.py
# Create your models here.


# 文章分类
class Category(models.Model):   # 文章分类
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 文章标签
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PostManager(models.Manager):
    """
       继承自默认的 Manager ，为其添加一个自定义的 archive 方法
       """
    def archive(self):
        date_list = Post.objects.datetimes('created_time', 'month', order='DESC')
        # 获取到降序排列的精确到月份且已去重的文章发表时间列表
        # 并把列表转为一个字典，字典的键为年份，值为该年份下对应的月份列表
        date_dict = defaultdict(list)
        for d in date_list:
            date_dict[d.year].append(d.month)
        # 模板不支持defaultdict，因此我们把它转换成一个二级列表，由于字典转换后无序，因此重新降序排序
        return sorted(date_dict.items(), reverse=True)


class Post(models.Model):  #自定义了 Manger 后需要在 model 中显示地指定它：
    # 文章标题
    objects = PostManager()  # 使用默认的 objects 作为 manager的名字
    title = models.CharField(max_length=70,verbose_name="文章标题")
    body = models.TextField(verbose_name="文章正体")
    created_time = models.DateTimeField(verbose_name="创建时间")
    modified_time = models.DateTimeField(verbose_name="修改时间", blank=True)
    excerpt = models.CharField(max_length=200, blank=True)
    views = models.PositiveIntegerField(default=0)  # 记录文章阅读量
    # 文章类别 category为外键 与Category关联
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 文章标签 tag为 多对多的关系
    tag = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # 获取访问的绝对地址
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])  # 只更新数据库中views字段的值

    def save(self,*args,**kwargs):  # 重写django的save方法
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化一个 markdown类，用于渲染 body的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]

            # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_time']