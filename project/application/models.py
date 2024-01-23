from django.db import models


class Main(models.Model):

    title = models.CharField('Название профессии', max_length=100)
    description = models.TextField('Описание')
    image = models.ImageField('Картинка', blank=True, upload_to='pictures/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"


class DemandChart(models.Model):

    title = models.CharField('Название графика', max_length=100)
    image = models.ImageField('График', upload_to='charts/')
    dict = models.JSONField('Таблица', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'График востребованности'
        verbose_name_plural = 'Графики востребованности'


class GeoChart(models.Model):

    title = models.CharField('Название графика', max_length=100)
    image = models.ImageField('График', upload_to='charts/')
    dict = models.JSONField('Таблица', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'График географии'
        verbose_name_plural = 'Графики географии'


class Skills(models.Model):

    title = models.CharField('Название графика', max_length=100, null=True)
    image = models.ImageField('График', upload_to='charts/', null=True)
    dict = models.JSONField('Таблица', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ключевой навык'
        verbose_name_plural = 'Ключевые навыки'
