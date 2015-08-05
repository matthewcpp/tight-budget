from django.apps import AppConfig

from django.db.models.signals import pre_save

class BudgetAPIConfig(AppConfig):
    name = 'budget_api'
    verbose_name = "Tight Budget REST API"

    def ready(self):
        from budget_api.signals import category_template_on_pre_save
        from budget_api.models import CategoryTemplate
        
        pre_save.connect(category_template_on_pre_save, dispatch_uid="CategoryTemplate_pre_save", sender=CategoryTemplate)