from rest_framework import serializers
from budget_api.models import BudgetTemplate, CategoryTemplate, Budget, Category, Transaction

class BudgetTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetTemplate
        fields = ('id', 'name', 'description', 'total_amount', 'created_time', 'updated_time')
        
class CategoryTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryTemplate
        fields = ('id', 'name', 'budget_template', 'description', 'allocated_amount', 'rollover', 'created_time', 'updated_time')

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ('id', 'name', 'description', 'total_amount', 'spent_amount', 'created_time', 'updated_time')
  
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'budget', 'description', 'allocated_amount', 'spent_amount', 'created_time', 'updated_time')
  
class BudgetDetailSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Budget
        fields = ('id', 'name', 'description', 'total_amount', 'spent_amount', 'categories', 'created_time', 'updated_time')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'name', 'category', 'description', 'amount', 'created_time', 'updated_time')