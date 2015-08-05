from django.db.models.signals import pre_save
from django.utils import timezone

from budget_api.models import CategoryTemplate


#   this callback updates the allocated amount for the Budget Template when
#   a CategoryTemplate is added or modified

def category_template_on_pre_save(sender, **kwargs):
    category_template = kwargs["instance"];
    budget_template = category_template.budget_template
    
    allocated_amount_difference = category_template.allocated_amount
    previous_allocated_amount = category_template.tracker.previous("allocated_amount")
    
    if previous_allocated_amount != None:
        allocated_amount_difference -= previous_allocated_amount
    
    budget_template.total_amount += allocated_amount_difference
    budget_template.updated_time = timezone.now()
    
    budget_template.save()

