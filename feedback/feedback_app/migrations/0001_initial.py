# Generated by Django 4.2.5 on 2023-09-09 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100, verbose_name='Страна')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=20, verbose_name='Оценка')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100, verbose_name='ФИО')),
                ('feedback', models.TextField(verbose_name='Отзыв')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback_app.countries', verbose_name='Страна')),
                ('rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback_app.rating', verbose_name='Оценка')),
            ],
        ),
    ]
