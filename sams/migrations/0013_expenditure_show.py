# Generated by Django 3.2.9 on 2022-03-29 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sams', '0012_expenditure'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenditure',
            name='show',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sams.show'),
        ),
    ]