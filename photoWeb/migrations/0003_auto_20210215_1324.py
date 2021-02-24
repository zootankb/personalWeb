# Generated by Django 3.1.6 on 2021-02-15 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photoWeb', '0002_auto_20210215_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cameraman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photoWeb.cameraman', verbose_name='摄影师'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photoWeb.category', verbose_name='风格'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(default='默认日志内容', max_length=1000, verbose_name='日志内容'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='imgLevel1',
            field=models.ImageField(help_text='最大尺寸', upload_to='', verbose_name='图片1'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='imgLevel2',
            field=models.ImageField(help_text='第二大尺寸', upload_to='', verbose_name='图片2'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='imgLevel3',
            field=models.ImageField(help_text='第三大尺寸', upload_to='', verbose_name='图片3'),
        ),
        migrations.AlterField(
            model_name='cameraman',
            name='name',
            field=models.CharField(default='Null', max_length=40, verbose_name='名字'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='默认风格', max_length=40, verbose_name='风格'),
        ),
    ]
