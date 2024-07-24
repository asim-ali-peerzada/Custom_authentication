# Generated by Django 5.0 on 2024-07-24 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internee_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_employee',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_manager',
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('manager', 'Manager'), ('employee', 'Employee'), ('user', 'User')], default='user', max_length=10),
        ),
    ]