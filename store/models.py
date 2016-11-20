from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length = 30)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'categories'

class Product(models.Model):
	name = models.CharField(max_length = 30)
	price = models.IntegerField()
	category = models.ForeignKey(Category)
	description = models.TextField()

	def __str__(self):
		return self.name