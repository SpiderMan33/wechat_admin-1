from time import timezone

from django.db import models

# Create your models here.
from django.utils.html import format_html
from django.utils.timezone import now


# class BaseEntity:
#     date_created = models.DateTimeField('创建时间', default=now())
#     date_modified = models.DateTimeField('更新时间', default=now())

class LoginUser(models.Model):
    name = models.CharField('用户名', max_length=100, unique=True)
    password = models.CharField('密码', max_length=100)
    enable = models.BooleanField('是否启用', default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '登录用户'
        verbose_name_plural = '登录用户'


class WeChatUser(models.Model):
    nickname = models.CharField('昵称', max_length=100, unique=True)
    alias = models.CharField('别名', max_length=100, unique=False)
    service_type = models.IntegerField('服务类型', default=1)
    fakeid = models.CharField('biz', max_length=100, default=None, unique=True)
    round_head_img = models.URLField('头像', max_length=500, default=None)
    crawl_history = models.BooleanField('是否爬取历史文章', default=False)
    crawled_history = models.BooleanField('是否爬取过历史文章', default=False)
    monitored = models.BooleanField('是否监控最新文章', default=False)
    description = models.CharField('描述', max_length=255, default=None)
    enable = models.BooleanField('是否启用', default=True)

    def __unicode__(self):
        return self.nickname

    def head_image(self):
        if self.round_head_img:
            return format_html('<img src="%s" />' % self.round_head_img)
        else:
            return '暂无头像'

    head_image.short_description = '头像'

    class Meta:
        verbose_name = '微信公众号'
        verbose_name_plural = '微信公众号'


class Keyword(models.Model):
    name = models.CharField('关键词', max_length=100, unique=True)
    enable = models.BooleanField('是否启用', default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '关键词'
        verbose_name_plural = '关键词'


class WeChatData(models.Model):
    title = models.CharField('标题', max_length=100)
    content = models.TextField('内容')
    like_num = models.IntegerField('点赞数', default=0)
    read_num = models.IntegerField('阅读量', default=0)
    url = models.URLField('链接', max_length=255, default=None, unique=True)
    pub_time = models.DateTimeField('发布时间', default=None)
    user = models.ForeignKey(WeChatUser)

    def __unicode__(self):
        return self.url

    class Meta:
        verbose_name = '微信文章'
        verbose_name_plural = '微信文章'
