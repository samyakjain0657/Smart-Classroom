# Generated by Django 2.1.3 on 2018-11-17 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('samyak', models.BooleanField(default=0)),
                ('shreyanshi', models.BooleanField(default=0)),
                ('apurva', models.BooleanField(default=0)),
                ('daman', models.BooleanField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
