from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Cameraman(models.Model):
    id = models.AutoField("摄影师ID", primary_key=True)
    name = models.CharField("名字", max_length=40, default="Null")
    description = models.TextField("介绍", max_length=400, default="无")
    mark = models.TextField("标注", max_length=400, default="默认标注")
    created_at = models.DateTimeField("添加日期", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = '摄影师信息表'
        verbose_name_plural = '摄影师信息表'


class Category(models.Model):
    id = models.AutoField("风格ID", primary_key=True)
    name = models.CharField("风格", max_length=40, default="默认风格")
    mark = models.TextField("标注", max_length=400, default="默认标注")
    created_at = models.DateTimeField("添加日期", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = '风格信息表'
        verbose_name_plural = '风格信息表'


class Blog(models.Model):
    id = models.AutoField("日志id", primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="风格")
    cameraman = models.ForeignKey(Cameraman, on_delete=models.CASCADE, verbose_name="摄影师")
    title = models.CharField("标题", max_length=100, default="默认标题")
    imgLevel1 = models.ImageField("图片1", upload_to="photo_web_img", help_text="最大尺寸")
    imgLevel2 = models.ImageField("图片2", upload_to="photo_web_img", help_text="第二大尺寸")
    imgLevel3 = models.ImageField("图片3", upload_to="photo_web_img", help_text="第三大尺寸")
    description = models.TextField("简介", max_length=400, default="无")
    content = models.TextField("日志内容", max_length=1000, default="默认日志内容")
    created_at = models.DateTimeField("添加日期", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = '日志信息表'
        verbose_name_plural = '日志信息表'


class FeedBack(models.Model):
    id = models.AutoField("反馈id", primary_key=True)
    name = models.TextField('名字', max_length=100, default='None', help_text='用户填的名字')
    email = models.EmailField('邮箱地址', max_length=254, help_text='O.O')
    message = models.TextField('反馈内容', max_length=2000, help_text='长度不确定，暂时设为最长2000')
    created_at = models.DateTimeField("添加日期", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = '反馈信息表'
        verbose_name_plural = '反馈信息表'
