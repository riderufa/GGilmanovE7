# Generated by Django 2.2.11 on 2020-03-31 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20200331_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='advert',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='board.Advert'),
        ),
    ]
