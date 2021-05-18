# Generated by Django 2.2 on 2021-05-18 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True)),
                ('location', models.CharField(blank=True, max_length=250)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('current_weight', models.IntegerField(blank=True, max_length=250)),
                ('goal_weight', models.IntegerField(blank=True, max_length=250)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='main_app.User')),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
