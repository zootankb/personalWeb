# Generated by Django 3.1.6 on 2021-02-22 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoWeb', '0005_auto_20210215_1811'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created_at'], 'verbose_name': '日志信息表', 'verbose_name_plural': '日志信息表'},
        ),
        migrations.AlterModelOptions(
            name='cameraman',
            options={'ordering': ['-created_at'], 'verbose_name': '摄影师信息表', 'verbose_name_plural': '摄影师信息表'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-created_at'], 'verbose_name': '风格信息表', 'verbose_name_plural': '风格信息表'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='imgLevel1',
            field=models.ImageField(help_text='最大尺寸', upload_to='photo_web_img', verbose_name='图片1'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='imgLevel2',
            field=models.ImageField(help_text='第二大尺寸', upload_to='photo_web_img', verbose_name='图片2'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='imgLevel3',
            field=models.ImageField(help_text='第三大尺寸', upload_to='photo_web_img', verbose_name='图片3'),
        ),
    ]
