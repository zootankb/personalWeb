# Generated by Django 3.1.6 on 2021-02-15 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoWeb', '0004_blog_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='imgLevel1',
            field=models.ImageField(help_text='最大尺寸', upload_to='img', verbose_name='图片1'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='imgLevel2',
            field=models.ImageField(help_text='第二大尺寸', upload_to='img', verbose_name='图片2'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='imgLevel3',
            field=models.ImageField(help_text='第三大尺寸', upload_to='img', verbose_name='图片3'),
        ),
    ]
