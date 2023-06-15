from django.db import models

# Create your models here.


'''谜语实体'''
class Riddle(models.Model):
    riddle_answer = models.CharField('谜语答案',max_length=30)
    riddle_type = models.CharField('谜语类型',max_length=30)
    riddle_description = models.CharField('谜语描述',max_length=30)

''' 比赛实体 '''
class Competition(models.Model):
    name = models.CharField('比赛名称',max_length=20)
    turn = models.IntegerField('比赛轮次')
    victor_name = models.CharField('胜利者名称',max_length=50,null=True,blank=True)
    start_date = models.DateTimeField('比赛开始时间')
    end_date = models.DateTimeField('比赛结束时间',null=True,blank=True)

'''比赛记录实体'''
class CompetitionRecord(models.Model):
    competition_id = models.ForeignKey(Competition,on_delete=models.CASCADE)
    participant_name = models.CharField('比赛参与者',max_length=50)
    score = models.IntegerField('比赛分数')

'''排行榜'''
class Leaderboard(models.Model):
    participant_name = models.CharField('比赛参与者',max_length=50)
    wins = models.IntegerField('获胜次数')
