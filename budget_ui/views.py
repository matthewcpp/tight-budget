from django.template.response import TemplateResponse
from django.views.generic import View

from rest_framework.renderers import JSONRenderer

from budget_api.models import Budget, Category
from budget_api.serializers import BudgetSerializer, CategorySerializer

class UiIndexView(View):
    def get(self, request):
        budget = Budget.objects.order_by("-updated_time")[:1][0]
        categories = budget.categories.all();
        
        budget_serializer = BudgetSerializer(budget)
        categories_serializer = CategorySerializer(categories, many=True)
        
        json_renderer = JSONRenderer();
        budget_json_data = json_renderer.render(budget_serializer.data)
        categories_json_data = json_renderer.render(categories_serializer.data)
        
        return TemplateResponse(request, 'budget_ui/index.html', {"budget_data": budget_json_data, "categories_data": categories_json_data})