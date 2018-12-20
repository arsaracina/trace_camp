# Generated by Django 2.0 on 2018-12-20 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KickStarter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buckers_count', models.IntegerField()),
                ('blurb', models.TextField()),
                ('category', models.TextField()),
            ],
            options={
                'ordering': ['buckers_count'],
            },
        ),
    ]
