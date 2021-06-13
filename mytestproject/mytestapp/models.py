from django.db import models
from datetime import datetime


class interviews(models.Model):

    iname = models.CharField(max_length=255, verbose_name="Название")
    bdate = models.DateField(default=datetime.today(),
                             verbose_name="дата старта")
    edate = models.DateField(verbose_name="дата окончание")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.iname+' '+str(self.bdate)

    class Meta:
        ordering = ['bdate']
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"


class questions(models.Model):

    interview = models.ForeignKey(
        interviews, on_delete=models.CASCADE, related_name="question")
    text = models.CharField(max_length=200, verbose_name="Текс вопроса")
    type = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "вопрос"
        verbose_name_plural = "вопросы"


class answers(models.Model):

    username = models.CharField(
        max_length=255, verbose_name="username", default="None")
    type = models.CharField(
        max_length=50, default="Not anonym", verbose_name="поля для типа ответа")
    question = models.ForeignKey(
        questions, on_delete=models.CASCADE, default=0)
    dates = models.DateField(default=datetime.today())
    text_q = models.CharField(
        max_length=255, verbose_name="свой ответ на вопрос", null=True)

    def __str__(self):
        return f" ответ пользователя {self.user} - {self.question} / {self.text_q}"

    class Meta:

        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
