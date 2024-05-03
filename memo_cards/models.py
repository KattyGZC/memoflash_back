from django.db import models
from users.models import User

class Topic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics', verbose_name='User')
    name = models.CharField('Name', max_length=255)
    enable = models.BooleanField('Enable', default=False)

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'

    def __str__(self):
        return self.name 
    
class Card(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="cards", verbose_name='Topic')
    created_at = models.DateTimeField('Created', auto_now_add=True)
    modified_at = models.DateTimeField('Modified', auto_now=True)

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'


class Item(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='items', verbose_name='Card')
    title = models.CharField('Title', max_length=255)
    content = models.TextField('Content')
    comment = models.TextField('Comment')

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'