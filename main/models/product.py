from django.db import models
from .material import Material

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('hot', 'Горячее блюдо'),
        ('cold', 'Холодное блюдо'),
    ]
    
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    category = models.CharField(
        'Категория',
        max_length=20,
        choices=CATEGORY_CHOICES
    )
    material = models.ForeignKey(
        Material,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Тип'
    )
    dimensions = models.CharField('Вес', max_length=50)
    image = models.ImageField('Изображение', upload_to='products/')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name