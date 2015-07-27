from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns
from budget_api import views

urlpatterns = [
    url(r'^budgets/$', views.BudgetList.as_view()),
    url(r'^budgets/(?P<pk>[0-9]+)/$', views.BudgetDetail.as_view()),
    url(r'^budgets/(?P<pk>[0-9]+)/categories/$', views.CategoryList.as_view()),
    url(r'^categories/(?P<pk>[0-9]+)/transactions$', views.CategoryTransactionList.as_view()),
    url(r'^transactions/(?P<pk>[0-9]+)/$', views.TransactionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)