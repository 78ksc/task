# Generated by Django 3.2.18 on 2023-08-05 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Intern_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_titel', models.CharField(blank=True, max_length=20, null=True)),
                ('i_desc', models.TextField(blank=True)),
                ('last_date', models.DateTimeField(blank=True)),
                ('vacancy', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_titel', models.CharField(blank=True, max_length=20, null=True)),
                ('job_desc', models.TextField(blank=True)),
                ('last_date', models.DateTimeField(blank=True)),
                ('vacancy', models.IntegerField(blank=True, null=True)),
                ('experience_required', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='X_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_titel', models.CharField(blank=True, max_length=20, null=True)),
                ('job_desc', models.TextField(blank=True)),
                ('last_date', models.DateTimeField(blank=True)),
                ('experience_required', models.IntegerField(blank=True, null=True)),
                ('change', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Xapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('xchange', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.x_post')),
            ],
        ),
        migrations.CreateModel(
            name='Japp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.job_post')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Iapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internship', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.intern_post')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]