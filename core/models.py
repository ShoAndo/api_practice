from django.db import models

class News(models.Model):
  day = models.DateTimeField('日')
  title = models.CharField('タイトル', max_length=128)
  body = models.TextField('内容')

  def to_dict(self):
    return {
      'id': self.id,
      'day': f"{self.day:%Y^%M^%d}",
      "title": self.title,
      "body": self.body,
    }

  class Meta:
    db_table = "news"
    ordering = ("-day",)

class Item(models.Model):
  name = models.CharField('商品名', max_length=128)
  description = models.TextField('商品説明')
  price = models.PositiveIntegerField('価格')

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'price': self.price,
      'description': self.description,
    }

    class Meta:
      db_table = 'item'
  

