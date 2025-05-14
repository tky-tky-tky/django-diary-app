# Django学習成果物：日記アプリ

このリポジトリは、Djangoの基礎学習として作成した日記アプリケーションです。  
簡単なCRUD機能（作成・表示・更新・削除）に加え、画像アップロードやログイン機能も実装しました。

未経験からWebフレームワークDjangoを学び、「実際に動くアプリケーションを一通り自作する」ことを目標としました。

---

## 主な機能

- 日記の投稿（タイトル、本文、画像の登録）
- 投稿一覧の表示
- 投稿の編集・削除機能
- ログイン・ログアウト機能

## 使用技術

- Python
- Django
- html

## 主に編集・追加したファイル

- `diary/models.py`：日記モデルの作成
- `diary/forms.py`：投稿用フォーム
- `diary/views.py`：一覧表示、新規作成、編集、削除の処理
- `diary/urls.py`：アプリ内URL定義
- `templates/`
  - `base.html`：共通レイアウト
  - `index.html`：トップページ
  - `diary_confirm_delete.html`：削除確認
  - `diary_detail.html`：日記確認
  - `diary_form.html`：作成フォーム
  - `diary_list.html`：投稿一覧
  - `diary_update.html`：編集フォーム
 
## ログイン情報（デモ用）

以下のアカウントでログインできます：
- ユーザー名：`test`
- パスワード：`test`
    
