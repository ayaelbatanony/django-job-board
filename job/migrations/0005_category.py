# Generated by Django 4.1 on 2022-08-15 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_job_experience_job_published_at_job_salary_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
    ]
