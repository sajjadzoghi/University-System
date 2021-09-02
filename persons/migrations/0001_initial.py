# Generated by Django 3.2.5 on 2021-09-01 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import persons.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('environment_education', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_id', models.IntegerField(default=persons.models.generateTeacherPersonalId, unique=True)),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='teachers/%Y/%m/%d')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='environment_education.college')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
            },
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_id', models.IntegerField(default=persons.models.generateStudentPersonalId, unique=True)),
                ('field', models.CharField(max_length=200)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='students/%Y/%m/%d')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], default='Male', max_length=10, null=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='environment_education.college')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
