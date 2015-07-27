from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from budget_api.models import Budget, Category, Transaction
from budget_api.serializers import BudgetSerializer, CategorySerializer, TransactionSerializer

class BudgetList(APIView):
    def get(self, request, format=None):
        budgets = Budget.objects.all()
        serializer = BudgetSerializer(budgets, many=True)
        
        return Response(serializer.data)
        
class BudgetDetail(APIView):
    def get(self, request, pk, format=None):
        budget = Budget.objects.get(pk=pk)
        serializer = BudgetSerializer(budget)
        
        return Response(serializer.data)
        
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
        
class TransactionDetail(APIView):
    def get(self, request, pk, format=None):
        transaction = Transaction.objects.get(pk=pk)
        serializer = TransactionSerializer(transaction)
        
        return Response(serializer.data)
        
    def delete(self, request, pk, format=None):
        transaction = None
        
        try:
            transaction = Transaction.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
        
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
        