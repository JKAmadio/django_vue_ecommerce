from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
		verbose_name_plural = "Categories"

class Product(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	description = models.TextField()
	price = models.DecimalField(max_digits=6, decimal_places=2)
	category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = ("Products")

	def __str__(self):
		return self.name

