# Generated by Django 3.2.3 on 2021-06-11 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('CompanyName', models.CharField(max_length=50)),
                ('Typeofbeer', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['id'],
                'unique_together': {('CompanyName', 'Typeofbeer')},
            },
        ),
        migrations.DeleteModel(
            name='Recruit',
        ),
    ]