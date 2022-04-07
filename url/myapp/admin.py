from django.contrib import admin

from myapp.models import LongToShort,ChartData
# Register your models here.

admin.site.register(LongToShort)
admin.site.register(ChartData)
