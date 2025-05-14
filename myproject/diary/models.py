from django.db import models
from pathlib import Path
import uuid # 被らないIDを作成

class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    # UUIDをプライマリキー、uuidを自動（デフォルト）設定、編集不可
    title = models.CharField(max_length=100, verbose_name="タイトル")
    body = models.TextField(max_length=2000, verbose_name="本文")
    page_date = models.DateTimeField(verbose_name="日付")
    picture = models.ImageField(
        upload_to="diary/picture/", blank=True, null=True, verbose_name="画像")
    # settings.pyで指定した更にサブフォルダのURL
    # blank=True, null=True 値がなくても可
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    # auto_now_add=True このデータが初めて作成された日時を保存
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
    # auto_now=True このデータが保存、更新される度に日時を保存
    """
    IntergerField = 数値
    FloatField = 小数点を含む数値
    EmailField = メールアドレス
    BooleanField = 真偽値
    TimeField = 時間
    FileField = ファイル
    ImageField = 画像
    ForeignKey = 外部キー
    """

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        picture = self.picture
        super().delete(*args, **kwargs)
        if picture:
            Path(picture.path).unlink(missing_ok=True)
    # deleteメソッドをオーバーライドする
    # 元々はページ削除しかできないため、画像も同時に削除する機能を追加
    # super().delete(*args, **kwargs)と関数内に記載して元々のdeleteの機能も保持
    # .unlink() = ファイルを削除 
    # missing_ok=True = ファイルが存在しない場合でもエラーにならない