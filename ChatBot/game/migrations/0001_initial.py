# Generated by Django 4.2.1 on 2023-06-15 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='比赛名称')),
                ('turn', models.IntegerField(verbose_name='比赛轮次')),
                ('victor_name', models.CharField(max_length=50, verbose_name='胜利者名称')),
                ('start_date', models.DateTimeField(verbose_name='比赛开始时间')),
                ('end_date', models.DateTimeField(verbose_name='比赛结束时间')),
            ],
        ),
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant_name', models.CharField(max_length=50, verbose_name='比赛参与者')),
                ('wins', models.IntegerField(verbose_name='获胜次数')),
            ],
        ),
        migrations.CreateModel(
            name='Riddle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('riddle_answer', models.CharField(max_length=30, verbose_name='谜语答案')),
                ('riddle_type', models.CharField(max_length=30, verbose_name='谜语类型')),
                ('riddle_description', models.CharField(max_length=30, verbose_name='谜语描述')),
            ],
        ),
        migrations.CreateModel(
            name='CompetitionRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant_name', models.CharField(max_length=50, verbose_name='比赛参与者')),
                ('score', models.IntegerField(verbose_name='比赛分数')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.competition')),
            ],
        ),
    ]
