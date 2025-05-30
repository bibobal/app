from django.db import models

class Material(models.Model):
    name = models.CharField('вид кофе', max_length=100, unique=True)
    description = models.TextField('Описание', blank=True)
    
    class Meta:
        verbose_name = 'вид кофе'
        verbose_name_plural = 'вид кофе'
        ordering = ['name']
    
    def __str__(self):
        return self.name