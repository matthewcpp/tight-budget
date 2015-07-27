from rest_framework import serializers
from budget_api.models import BudgetTemplate, CategoryTemplate, Budget, Category, Transaction

class BudgetTemplate(serializers.ModelSerializer):
    class Meta:
        model = BudgetTemplate
        fields = ('id', 'name', 'description', 'created_time', 'updated_time')
        
class CategoryTemplate(serializers.ModelSerializer):
    class Meta:
        model = CategoryTemplate
        fields = ('id', 'name', 'description', 'allocated_amount', 'rollover', 'created_time', 'updated_time')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'name', 'description', 'amount', 'budget_item', 'created_time', 'updated_time')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'allocated_amount', 'spent_amount', 'created_time', 'updated_time')

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ('id', 'name', 'description', 'total_amount', 'spent_amount', 'created_time', 'updated_time')