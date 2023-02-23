from django.contrib import admin
from .models import User_addon,Software,Usage,Sales,Subscription,Customer_Support


admin.site.register(User_addon)
admin.site.register(Software)
admin.site.register(Usage)
admin.site.register(Sales)
admin.site.register(Subscription)
admin.site.register(Customer_Support)
