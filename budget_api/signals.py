from django.db.models.signals import pre_save
from django.utils import timezone

from budget_api.models import CategoryTemplate


#   this callback updates the total amount for the Budget Template when
#   a CategoryTemplate is added or modified
def category_template_on_pre_save(sender, **kwargs):
    category_template = kwargs["instance"]
    
    if category_template.tracker.has_changed("allocated_amount"):
        budget_template = category_template.budget_template
        
        allocated_amount_difference = category_template.allocated_amount
        previous_allocated_amount = category_template.tracker.previous("allocated_amount")
        
        if previous_allocated_amount != None:
            allocated_amount_difference -= previous_allocated_amount
        
        budget_template.total_amount += allocated_amount_difference
        
        budget_template.updated_time = timezone.now()
        budget_template.save()


#   this callback updates the total and spent amounts for the Budget when
#   a Category is added or updated
def category_on_pre_save(sender, **kwargs):
    category = kwargs["instance"]
    
    budget = None
    needs_update = False
    
    #update allocated amount
    if category.tracker.has_changed("allocated_amount"):
        needs_update = True
        budget = category.budget
        
        allocated_amount_difference = category.allocated_amount
        previous_allocated_amount = category.tracker.previous("allocated_amount")
        
        if previous_allocated_amount != None:
            allocated_amount_difference -= previous_allocated_amount
            
        budget.total_amount += allocated_amount_difference
    
    #update spent amount
    if category.tracker.has_changed("spent_amount"):
        needs_update = True
        if budget is None:
            budget = category.budget
            
        spent_amount_difference = category.spent_amount
        previous_spent_amount = category.tracker.previous("spent_amount")
        
        if previous_spent_amount != None:
            spent_amount_difference -= previous_spent_amount
            
        budget.spent_amount += spent_amount_difference
    
    if needs_update:
        budget.updated_time = timezone.now()
        budget.save()
        
#   this callback updates the spent amount for the Category when
#   a Transaction is added or updated
def transaction_on_pre_save(sender, **kwargs):
    transaction = kwargs["instance"]
    
    if transaction.tracker.has_changed("amount"):
        category = transaction.category
        
        transaction_amount_difference = transaction.amount
        previous_transaction_amount = transaction.tracker.previous("amount")
        
        if previous_transaction_amount != None:
            transaction_amount_difference -= previous_transaction_amount
            
        category.spent_amount += transaction_amount_difference
        
        category.updated_time = timezone.now()
        category.save()
