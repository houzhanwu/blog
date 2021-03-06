# Generated by Django 2.0.7 on 2018-08-01 03:48

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('types', models.CharField(max_length=20)),
                ('is_show', models.BooleanField(default=False)),
                ('desc', models.CharField(max_length=100, null=True)),
                ('content', DjangoUeditor.models.UEditorField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='AType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=10)),
                ('f_typeid', models.IntegerField()),
            ],
            options={
                'db_table': 'article_type',
            },
        ),
    ]
