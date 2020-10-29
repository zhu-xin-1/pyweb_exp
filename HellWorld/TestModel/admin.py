from django.contrib import admin
from TestModel.models import Test,Contact,Tag
# Register your models here.
# 自定义表单 设定需要输入的内容
# class ContactAdmin(admin.ModelAdmin):
#     fields = ('name','email')
#
# admin.site.register([Test,Tag])
# admin.site.register(Contact,ContactAdmin)

# # 将自定义表单的输入也可以分栏 并定义自己的格式
# class ContactAdmin(admin.ModelAdmin):
#     fieldsets = (
#         ['Main', {
#             'fields': ('name','email'),
#         }],
#         ['Advance', {
#             'classes': ('collapse',),
#             'fields': ('age',),
#         }],
#     )
#
# admin.site.register(Contact,ContactAdmin)
# admin.site.register([Test, Tag])

# 内联显示
class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    fieldsets = (
        ['Main', {
            'fields': ('name','email'),
        }],
        ['Advance', {
            'classes': ('collapse',),
            'fields': ('age',),
        }],
    )

admin.site.register(Contact,ContactAdmin)
admin.site.register([Test])
