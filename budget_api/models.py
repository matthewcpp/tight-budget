from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group

from model_utils import FieldTracker

class BudgetTemplate(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    
    total_amount = models.FloatField(default=0.0)
    
    created_time = models.DateTimeField(default=timezone.now)
    updated_time = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return '%d: %s' % (self.id, self.name)

class CategoryTemplate(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    budget_template = models.ForeignKey(BudgetTemplate)
    
    allocated_amount = models.FloatField()
    rollover = models.BooleanField(default=False)
    
    created_time = models.DateTimeField(default=timezone.now)
    updated_time = models.DateTimeField(default=timezone.now)
    
    tracker = FieldTracker(fields=['allocated_amount'])
    
    def __str__(self):
        return '%d: %s' % (self.id, self.name)

class Budget(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    total_amount = models.FloatField(default=0.0)
    spent_amount = models.FloatField(default=0.0)
    
    created_time = models.DateTimeField(default=timezone.now)
    updated_time = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return '%d: %s' % (self.id, self.name)

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    
    budget = models.ForeignKey(Budget)
    
    allocated_amount = models.FloatField()
    spent_amount = models.FloatField(default=0.0)
    
    created_time = models.DateTimeField(default=timezone.now)
    updated_time = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return '%d: %s' % (self.id, self.name)
    
class Transaction(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    
    amount = models.FloatField()
    category = models.ForeignKey(Category)
    
    created_time = models.DateTimeField(default=timezone.now)
    updated_time = models.DateTimeField(default=timezone.now)
    
    tracker = FieldTracker(fields=['amount'])
    
    def __str__(self):
        return '%d: %s' % (self.id, self.name)
