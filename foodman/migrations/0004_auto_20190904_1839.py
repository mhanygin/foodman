# Generated by Django 2.2.4 on 2019-09-04 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodman', '0003_meal2dish_meals'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredients',
            old_name='desc',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='recipes',
            old_name='desc',
            new_name='description',
        ),
    ]
