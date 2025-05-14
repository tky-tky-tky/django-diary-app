#管理サイトを作成

from django.contrib import admin
from .models import Page


@admin.register(Page) # admin.site.register(Page, PageAdmin)と同義
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ["id", "created_at", "updated_at"]
    # 読み込み専用欄にmodelsで生成した内容を返す