# Generated by Django 2.2.4 on 2019-09-04 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodman', '0002_auto_20190904_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Meal2Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='foodman.Dishes')),
                ('meal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodman.Meals')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]