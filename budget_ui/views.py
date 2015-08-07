from django.template.response import TemplateResponse
from django.views.generic import View

from rest_framework.renderers import JSONRenderer

from budget_api.models import Budget, Category, Transaction
from budget_api.serializers import BudgetDetailSerializer

class UiIndexView(View):
    def get(self, request):
        budget = Budget.objects.order_by("-updated_time")[:1][0]
        serializer = BudgetDetailSerializer(budget)
        json_data = JSONRenderer().render(serializer.data)
        return TemplateResponse(request, 'budget_ui/index.html', {"budget_data": json_data})
        
class UiBudgetsListView(View):
    def get(self, request):
        budgets = Budget.objects.order_by("-updated_time")[:15]
        return TemplateResponse(request, 'budget_ui/budget_list.html', {"budget_list": budgets})
        
class UiBudgetsDetailView(View):
    def get(self, request, pk):
        budget = Budget.objects.get(pk=pk)
        categories = budget.category_set.all()
        
        return TemplateResponse(request, 'budget_ui/budget_detail.html', {"budget": budget, "categories": categories})
        
class UiCategoryDetailView(View):
    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        transactions = category.transaction_set.all()
        
        return TemplateResponse(request, 'budget_ui/category_detail.html', {"category": category, "transactions": transactions})
