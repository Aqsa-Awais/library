# Generated by Django 3.2.6 on 2021-08-16 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libraryproject', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cabinets',
            old_name='racks',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='racks',
            old_name='books',
            new_name='name',
        ),
        migrations.AddField(
            model_name='books',
            name='rack',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='libraryproject.racks'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='racks',
            name='cabinet',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='libraryproject.cabinets'),
            preserve_default=False,
        ),
    ]