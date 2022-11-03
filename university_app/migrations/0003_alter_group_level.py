# Generated by Django 4.1.2 on 2022-11-02 10:46

from django.db import migrations, models
import university_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('university_app', '0002_alter_group_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='level',
            field=models.CharField(choices=[(1, 'FirstClass'), (2, 'SecondClass'), (3, 'ThirdClass'), (4, 'MasterClass'), (5, 'DoctoralClass')], default=university_app.models.StudyLevel['FirstClass'], max_length=100),
        ),
    ]