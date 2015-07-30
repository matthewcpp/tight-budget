from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from budget_api.models import Budget, Category, Transaction, BudgetTemplate, CategoryTemplate
from budget_api.serializers import BudgetTemplateSerializer, CategoryTemplateSerializer, BudgetSerializer, CategorySerializer, TransactionSerializer

#---------------BugetTemplates

class BudgetTemplateList(APIView):
    def get(self, request, format=None):
        budgetTemplates = BudgetTemplate.objects.all()
        serializer = BudgetTemplateSerializer(budgetTemplates, many=True)
        
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = BudgetTemplateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class BudgetTemplateDetail(APIView):
    def get(self, request, pk, format=None):
        budgetTemplate = BudgetTemplate.objects.get(pk=pk)
        serializer = BudgetTemplateSerializer(budgetTemplate)
        
        return Response(serializer.data)
        
    def delete(self, request, pk, format=None):
        budgetTemplate = BudgetTemplate.objects.get(pk=pk)
        budgetTemplate.categorytemplate_set.all().delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class BudgetTemplateCategoryList(APIView):
    def get(self, request, pk, format=None):
        budgetTemplate = BudgetTemplate.objects.get(pk=pk)
        
        serializer = CategoryTemplateSerializer(budgetTemplate.categorytemplate_set.all(), many=True)
        return Response(serializer.data)
        
#---------------CategoryTemplates
        
        
class CategoryTemplateList(APIView):
    def post(self, request, format=None):
        serializer = CategoryTemplateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            category_template = serializer.instance
            budget_template = category_template.budget_template
            
            budget_template.total_amount += category_template.allocated_amount
            budget_template.updated_time = timezone.now()
            
            budget_template.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
      
class CategoryTemplateDetail(APIView):
    def delete(self, request, pk, format=None):
        categoryTemplate = CategoryTemplate.objects.get(pk=pk)
        categoryTemplate.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
        

#---------------Budgets

class BudgetList(APIView):
    def get(self, request, format=None):
        budgets = Budget.objects.all()
        serializer = BudgetSerializer(budgets, many=True)
        
        return Response(serializer.data)
        
    def post(self, request, format=None):
        budget_template_id = request.data.get("budget_template")
        
        if budget_template_id == None:
            serializer = BudgetSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            budget_template = BudgetTemplate.objects.get(pk=budget_template_id)
            category_templates = budget_template.categorytemplate_set.all()
            
            budget = Budget(name=budget_template, description=budget_template.description, total_amount=budget_template.total_amount)
            budget.save()
            
            for category_template in category_templates:
                budget.category_set.create(name=category_template.name, description=category_template.description, allocated_amount=category_template.allocated_amount)
            
            serializer = BudgetSerializer(budget)
            return Response(serializer.data)
        
class BudgetDetail(APIView):
    def get(self, request, pk, format=None):
        budget = Budget.objects.get(pk=pk)
        serializer = BudgetSerializer(budget)
        
        return Response(serializer.data)
        
#---------------Categories
        
class CategoryList(APIView):
    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, pk, format=None):
        budget = Budget.objects.get(pk=pk)
        categories = budget.category_set.all()
        serializer = CategorySerializer(categories, many=True)
        
        return Response(serializer.data)
        
#---------------Transactions
        
class TransactionDetail(APIView):
    def get(self, request, pk, format=None):
        transaction = Transaction.objects.get(pk=pk)
        serializer = TransactionSerializer(transaction)
        
        return Response(serializer.data)
        
    def delete(self, request, pk, format=None):
        transaction = None
        
        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            raise Http404
        
        #add the value of this transaction back to its category
        category = transaction.category
        category.spent_amount -= transaction.amount
        category.updated_time = timezone.now()
        category.save()
        
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


class CategoryTransactionList(APIView):  
    def get(self, request, pk, format=None):
        category = Category.objects.get(pk=pk)
        transactions = category.transaction_set.all()
        serializer = TransactionSerializer(transactions, many=True)
        
        return Response(serializer.data)
        
    def post(self, request, pk, format=None):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            transaction = serializer.instance
            category = transaction.category
            
            category.spent_amount += transaction.amount
            category.updated_time = timezone.now()
            category.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        