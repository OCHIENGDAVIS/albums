from django.db import models


class Expense(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    note = models.CharField(max_length=200, null=True, blank=True)
    amount = models.DecimalField(max_digits=19, decimal_places=2,null=True,blank=True)
    createdAt = models.DateTimeField(auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.description


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    marked = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




