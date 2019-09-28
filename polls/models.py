import datetime

from django.db import models
from django.utils import timezone


# 2 пустые строки после импортов,и дальше идут определения классов. удали повторящиеся импорты.
# ок.стоп. а не,показалось. сейчас нужно снова создать миграции. я сам
class Question(models.Model):
    """Вопрос для голосования"""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
   
    def __str__(self):
        return self.question_text
 
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    """Вариант ответа на вопрос"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


## не надо было добавлять новый код как в журнал., нужно было расширять текущую модель выше)  понятно? не очень
#  все что ниже касается модели вопроса и choise (__str__) перенеси в модели выше. сам) жду. объясни как.
# как я выже сделас с другим методом.stop) не все сразу,а по отдельныс методам. так стоп ща покажу где?
# короче там была модель просто Question: и все. ок. я буду ставить курсор, а ты копируй мето,
# дальше я скаху куда его ставить , жми ктрл+икс) чег
