from django.contrib import admin
from holidays.models import packages,order,hotels,transport,userinfo,blogs,comments


class userinfA(admin.ModelAdmin):
    list_display = ('users','address','mobile_no','pincode','country','datetime')
class packagesdisplay(admin.ModelAdmin):
        list_display = ('package_name','package_type','package_categories','package_duration','package_price')
# Register your models here.
admin.site.register(packages,packagesdisplay)
admin.site.register(order)
admin.site.register(hotels)
admin.site.register(transport)
admin.site.register(userinfo,userinfA)
admin.site.register(blogs)
admin.site.register(comments)
######admin customization

admin.site.site_header="Tourastic Holidays"