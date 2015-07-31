from django.template.response import TemplateResponse

from django.views.generic import View

from budget_api.models import Budget, Category

class UiIndexView(View):
    def get(self, request):
        return TemplateResponse(request, 'budget_ui/index.html', {})
        
class UiBudgetsListView(View):
    def get(self, request):
        return TemplateResponse(request, 'budget_ui/budget_list.html', {"budget_list": Budget.objects.all()})
        
class UiBudgetsDetailView(View):
    def get(self, request, pk):
        budget = Budget.objects.get(pk=pk)
        categories = budget.category_set.all()
        
        return TemplateResponse(request, 'budget_ui/budget_detail.html', {"budget": budget, "categories": categories})
