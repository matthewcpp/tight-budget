from django.apps import AppConfig

from django.db.models.signals import pre_save

class BudgetAPIConfig(AppConfig):
    name = 'budget_api'
    verbose_name = "Tight Budget REST API"

    def ready(self):
        from budget_api import signals as budget_signals
        from budget_api.models import CategoryTemplate, Category, Transaction
        
        pre_save.connect(budget_signals.category_template_on_pre_save, dispatch_uid="CategoryTemplate_pre_save", sender=CategoryTemplate)
        pre_save.connect(budget_signals.category_on_pre_save, dispatch_uid="Category_pre_save", sender=Category)
        pre_save.connect(budget_signals.transaction_on_pre_save, dispatch_uid="Transaction_pre_save", sender=Transaction)