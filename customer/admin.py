from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from customer import models as customer_model
# Register your models here.


class AddressAdmin(ImportExportModelAdmin):
    list_display=['user','full_name']

class wishlistAdmin(ImportExportModelAdmin):
    list_display=['user','product']

class NotificationAdmin(ImportExportModelAdmin):
    list_display =['user','type','seen','date']


admin.site.register(customer_model.Address,AddressAdmin)
admin.site.register(customer_model.Wishlist,wishlistAdmin)
admin.site.register(customer_model.Notification,NotificationAdmin)

