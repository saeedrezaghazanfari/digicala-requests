from django.db import models


class DigicalaModel(models.Model):
    category = models.ForeignKey('CategoryModel', on_delete=models.SET_NULL, blank=True, null=True)
    link_page = models.TextField()
    image = models.TextField()
    title = models.CharField(max_length=255)
    properties = models.TextField()
    seller = models.CharField(max_length=255)
    guarantee = models.CharField(max_length=255)
    price = models.PositiveBigIntegerField()

    def __str__(self):
        return self.title


class CategoryModel(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title