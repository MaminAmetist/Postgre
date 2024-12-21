from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    content = models.TextField('Текст')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'новость'
        ordering = ['-date']