# Generated by Django 3.1.7 on 2021-05-26 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_remove_courses_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='body',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='courses',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='title',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='regester',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]