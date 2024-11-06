from django.contrib import admin
from store import models as store_models
# Register your models here.

class GalleryInline(admin.TabularInline):
    model  =store_models.Gallery

class VarientInline(admin.TabularInline):
    model  =store_models.Variant

class VarientItemInline(admin.TabularInline):
    model  = store_models.VariantItem

class CategoryAdmin(admin.ModelAdmin):
    list_display =['title','image']
    list_editable=['image']
    prepopulated_fields ={ 'slug':('title',)}

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','category','regular_price','stock','status','features','vendor','date']
    search_fields =['name','category.title']
    list_filter =['status','features','category']
    inlines =[GalleryInline, VarientInline]
    prepopulated_fields={'slug':('name',)}

class VarientAdmin(admin.ModelAdmin):
    list_display=['product','name']
    search_fields =['product__name','name']
    inlines =[ VarientItemInline]

class VarientItemAdmin(admin.ModelAdmin):
    list_display=['varient','title','content']
    search_fields =['varient.name','name']

class GalleryAdmin(admin.ModelAdmin):
    list_display=['product','gallery_id']
    search_fields=['product.name','gallery_id']


class CartAdmin(admin.ModelAdmin):
    list_display=['cart_id','product','user','qty','price','total','date']
    search_fields =['cart_id','product.name','user.name']

class CouponAdmin(admin.ModelAdmin):
    list_display=['vendor','code','discount']
    search_fields =['code','vendor.username']

class OrderAdmin(admin.ModelAdmin):
    list_display=['order_id','customer','total','payment_status','order_status','payment_method','payment_id','date']
    list_editable =['payment_status','order_status','payment_method']
    search_fields =['order_id','customer.username']
    list_filter =['payment_status','order_status']

class OrderItemAdmin(admin.ModelAdmin):
    list_display=['item_id','order','product','qty','price','total']
    search_fields =['item_id','order.order_id','product.name']
    list_filter =['order__date']

class ReviewAdmin(admin.ModelAdmin):
    list_display=['user','product','rating','active','date','review']
    search_fields =['user.username','product.name']
    list_filter =['active','rating']

admin.site.register(store_models.Category,CategoryAdmin)
admin.site.register(store_models.Product,ProductAdmin)
admin.site.register(store_models.Variant,VarientAdmin)
admin.site.register(store_models.VariantItem,VarientItemAdmin)
admin.site.register(store_models.Gallery,GalleryAdmin)
admin.site.register(store_models.Cart,CartAdmin)
admin.site.register(store_models.Coupon,CouponAdmin)
admin.site.register(store_models.Order,OrderAdmin)
admin.site.register(store_models.OrderItem,OrderItemAdmin)
admin.site.register(store_models.Review,ReviewAdmin)