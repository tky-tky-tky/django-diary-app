#url.pyから呼び出され、ブラウザにレスポンスを返す
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin #ログインを必須にするMixin
from django.views import View # 汎用的なView用の基底クラス
from .forms import PageForm
from .models import Page
from datetime import datetime
from zoneinfo import ZoneInfo

# LoginRequiredMixinは必ず一番最初に追加する必要がある
class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        # 日記アプリのトップページにアクセスした時に動くメソッド
        # request = ユーザーから送られてきたデータを含む

        datetime_now = datetime.now(
                ZoneInfo("Asia/Tokyo")
        ).strftime("%Y年%m月%d日 %H:%M:%S")
        #pythonの処理をhtmlに送ることが可能

        return render(
            request, "diary/index.html",
            {"datetime_now": datetime_now}, # {HTML側の変数:Python側の変数}の辞書
            )
        # render = 画面のレスポンスを返す
        # 返す画面のhtmlを指定

class PageCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = PageForm()
        return render(request, "diary/page_form.html", {"form": form})
        # render(リクエストに対して, 表示するページ, htmlに対応した辞書データ)
    
    def post(self, request):# 保存に対して動くメソッド
        form = PageForm(request.POST, request.FILES)
        if form.is_valid(): # チェックするメッソド。問題なければ保存
            form.save()
            return redirect("diary:index") # diaryアプリ内の名前indexを指定
            # POSTの重複を防ぐため転送が必須
        return render(request, "diary/page_form.html", {"form": form})


class PageListView(LoginRequiredMixin, View):
    def get(self, request):
        page_list = Page.objects.order_by("-page_date") 
        # objects.all() = DBから日記データを全て取得
        # objects.order_by() = ソートする -を付けると降順
        return render(request, "diary/page_list.html", {"page_list": page_list})

class PageDetailView(LoginRequiredMixin, View):
    def get(self, request, id):
        page_detail = get_object_or_404(Page, id=id) 
        # DBからIDが一致するPageのデータを取得 or 404ページ
        return render(request, "diary/page_detail.html", {"page_detail": page_detail})
    

class PageUpdateView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id) 
        form = PageForm(instance=page)
        # 取得したページ内容をformに含めて取得
        return render(request, "diary/page_update.html", {"form": form})
    
    def post(self, request, id):
        page = get_object_or_404(Page, id=id) 
        form = PageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            form.save()
            return redirect("diary:page_detail", id=id)
        return render(request, "diary/page_update.html", {"form": form})
    
class PageDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id) 
        return render(request, "diary/page_confirm_delete.html", {"page": page})

    def post(self, request, id):
        page = get_object_or_404(Page, id=id) 
        page.delete()
        return redirect('diary:page_list')
        


index = IndexView.as_view()
    #as_view() = IndexViewクラスを関数に変換(getメソットが動く)
page_create = PageCreateView.as_view()
page_list = PageListView.as_view()
page_detail = PageDetailView.as_view()
page_update = PageUpdateView.as_view()
page_delete = PageDeleteView.as_view()