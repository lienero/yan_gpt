# Generated by Django 4.2 on 2023-05-17 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='닉네임')),
                ('ai_liked', models.IntegerField(default=0, verbose_name='ai의 호감도')),
                ('common_event_flag', models.IntegerField(default=0, verbose_name='공통 이벤트 플래그')),
                ('yan_event_flag', models.IntegerField(default=0, verbose_name='YAN 이벤트 플래그')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255, verbose_name='메시지')),
                ('from_ai', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yangpt_app.user')),
            ],
            options={
                'db_table': 'chats',
            },
        ),
    ]
