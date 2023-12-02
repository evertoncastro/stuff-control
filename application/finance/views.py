from django.shortcuts import render
from rest_framework import viewsets
from .models import Expense
from .serializers import ExpenseSerializer


class ExpenseView(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()


def index(request):
    expenses = Expense.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'expenses': expenses})


def create_expense(request):
    title = request.POST.get('title')
    expense = Expense.objects.create(title=title)
    expense.save()
    expenses = Expense.objects.all().order_by('-created_at')
    return render(request, 'expense-list.html', {'expenses': expenses})


def mark_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    expense.checked = True
    expense.save()
    expenses = Expense.objects.all().order_by('-created_at')
    return render(request, 'expense-list.html', {'expenses': expenses})


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    expense.delete()
    expenses = Expense.objects.all().order_by('-created_at')
    return render(request, 'expense-list.html', {'expenses': expenses})