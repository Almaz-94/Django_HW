from django.contrib import admin

from newsletter.models import Newsletter, Letter, Client,  NLLogs #NLStatus,

# Register your models here.

@admin.register(Newsletter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('pk','start','end','period','status','letter')
    list_filter = ('start','end','period','status')
    search_fields = ('period','status')

@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ('pk','head','body')
    search_fields = ('head','body')

# @admin.register(NLStatus)
# class NKStatusAdmin(admin.ModelAdmin):
#     list_display = ('status',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name','email','comment')
    search_fields = ('name','email','comment')

@admin.register(NLLogs)
class NLLogs(admin.ModelAdmin):
    readonly_fields = ('last_try', 'status')
    list_display = ('newsletter', 'last_try', 'status',)
