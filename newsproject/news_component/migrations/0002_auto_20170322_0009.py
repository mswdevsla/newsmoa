# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_component', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newscontent',
            name='news_company',
            field=models.IntegerField(choices=[(1, '조선일보'), (2, '동아일보'), (3, '한겨레'), (4, '중앙일보')]),
        ),
        migrations.AlterField(
            model_name='newscontent',
            name='news_section',
            field=models.IntegerField(choices=[(1, '정치'), (2, '경제'), (3, '사회'), (4, '국제')]),
        ),
    ]