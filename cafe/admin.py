from django.contrib import admin

# Register your models here.
from cafe.models import User, Table, MenuItem, Orders, Receipts

admin.site.register(User)
admin.site.register(Table)
admin.site.register(MenuItem)
admin.site.register(Orders)
admin.site.register(Receipts)
