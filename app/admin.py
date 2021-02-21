from django.contrib import admin
from .models import Fund, Expense, Category

admin.site.register(Fund)
admin.site.register(Expense)
admin.site.register(Category)
