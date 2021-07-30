from django.contrib import admin

# Register your models here.
from cafe.models import User, Table, MenuItem, Orders, Receipts

admin.site.register(User)
admin.site.register(Table)
# admin.site.register(MenuItem)
#admin.site.register(Orders)
admin.site.register(Receipts)


class MenuItemAdmin(admin.ModelAdmin):
    readonly_fields = ('creat_time_stamp','modified_time_stamp',)



admin.site.register(MenuItem, MenuItemAdmin)

def delete_order(modeladmin,request,queryset):
    queryset.update(status='d')
delete_order.short_description='marke selected as deleted'

class Orderadmin(admin.ModelAdmin):
    actions=[delete_order]
admin.site.register(Orders,Orderadmin)