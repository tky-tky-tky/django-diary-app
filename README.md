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
  
## スクリーンショット
![2025y05m15d_044012000](https://github.com/user-attachments/assets/eac8c804-ab6d-4f1e-9b86-8b578aa6fcd4)
![2025y05m15d_044007449](https://github.com/user-attachments/assets/3c219afb-f7ca-4e85-b161-0d6e5af118e3)
![2025y05m15d_044003784](https://github.com/user-attachments/assets/7186c6f9-71d3-43a6-bba9-4c276a537dd4)
![2025y05m15d_043959082](https://github.com/user-attachments/assets/f6f4ff1d-c3c9-4f00-8953-e78f5f105cc8)
![2025y05m15d_043955034](https://github.com/user-attachments/assets/9b69343a-f008-4e05-ba09-794dc9e7da8e)
![2025y05m15d_043948998](https://github.com/user-attachments/assets/9aa58a73-8ed4-4def-b379-7153475bf892)
![2025y05m15d_043942630](https://github.com/user-attachments/assets/4a4284d3-aa60-4dc8-9590-8f3db002195d)

