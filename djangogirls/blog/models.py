from django.conf import settings
#fromで指定したところからimportで必要な部分を借りてくる
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #models.ForeignKeyは他のモデルへのリンク
    title = models.CharField(max_length=200)
    #models.CharFieldは文字数が制限されたテキストを定義するフィールド
    text = models.TextField()
    #models.TextFieldは制限無しの長いテキスト用のフィールド
    created_date = models.DateTimeField(default=timezone.now)
    #models.DateTimeFieldは日付と時間のフィールド
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        #def publish(self):は今回作るブログを公開するメソッド
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title