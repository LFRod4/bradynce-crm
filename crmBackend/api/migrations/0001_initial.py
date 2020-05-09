# Generated by Django 2.1.1 on 2020-05-05 01:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_first_name', models.CharField(max_length=125)),
                ('lead_last_name', models.CharField(max_length=125)),
                ('email', models.CharField(max_length=125)),
                ('phone', models.IntegerField()),
                ('source', models.CharField(max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=125)),
                ('last_name', models.CharField(max_length=125)),
                ('email', models.CharField(max_length=125)),
                ('signed_up', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='lead',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
    ]