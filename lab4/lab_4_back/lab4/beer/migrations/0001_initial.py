# Generated by Django 3.2.3 on 2021-06-11 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('CompanyName', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]