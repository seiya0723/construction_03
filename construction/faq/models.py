from django.db import models
from django.utils import timezone

from django.conf import settings
from django.core.validators import MinValueValidator

class Question(models.Model):


    def day_after_tomorrow():
        return timezone.now() + timezone.timedelta(days=2)

    title       = models.CharField(verbose_name="質問タイトル",max_length=50)
    dt          = models.DateTimeField(verbose_name="質問投稿日時",default=timezone.now)
    content     = models.CharField(verbose_name="質問内容",max_length=2000)

    #質問の受付期限(手動で延長することもできる)
    accept_dt   = models.DateTimeField(verbose_name="質問受付期限",validators=[ MinValueValidator(day_after_tomorrow) ])

    #カスタムユーザーモデルと1対多のリレーションを組む
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="質問者",on_delete=models.CASCADE)

    #TODO:この質問に対して寄せられた回答数をカウントするメソッド
    #TODO:この質問に対して寄せられた回答を出力するメソッド

class Answer(models.Model):

    dt          = models.DateTimeField(verbose_name="回答投稿日時",default=timezone.now)
    content     = models.CharField(verbose_name="回答内容",max_length=2000)

    question    = models.ForeignKey(Question,verbose_name="対象の質問",on_delete=models.CASCADE)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="回答者",on_delete=models.CASCADE)


class Reply(models.Model):

    dt          = models.DateTimeField(verbose_name="リプライ投稿日時",default=timezone.now)
    content     = models.CharField(verbose_name="リプライ内容",max_length=2000)

    answer      = models.ForeignKey(Answer,verbose_name="対象の回答",on_delete=models.CASCADE)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="リプライ者",on_delete=models.CASCADE)






class AnswerUser(models.Model):

    #会員登録時、作ってすぐのユーザーIDをココに入れる。
    user        = models.OneToOneField(settings.AUTH_USER_MODEL,verbose_name="ユーザー",on_delete=models.CASCADE)

    company     = models.CharField(verbose_name="所属会社名",max_length=200)
    approval    = models.BooleanField(verbose_name="回答権利",default=False)




class QuestionUser(models.Model):

    user        = models.OneToOneField(settings.AUTH_USER_MODEL,verbose_name="ユーザー",on_delete=models.CASCADE)

    seriousness = models.CharField(verbose_name="購入の本気度",max_length=200)





#TODO:メールアドレスが確認済みかどうかチェックしたい場合、
# https://github.com/pennersr/django-allauth/blob/d367458580f5ebe6e6a0903ba78f85e2e082e0f2/allauth/account/models.py#L15 に書かれてある、EmailAddress モデルを参照する


"""

#allauthのEmailAddressモデルにメールの確認状態を記録するフィールドverifiedがある
from allauth.account.models import EmailAddress


# 中略 #
if not EmailAddress.objects.filter(user=request.user.id, verified=True):
    #メールの確認をしていない場合、確認するページにリダイレクトする
    return redirect("account_email_verification_sent")


#TODO:上記を全てのビューに貼り付ける。手間になるのであれば、LoginRequiredMixinをオーバーライドして認証状態チェックとセットでメール確認をする。それも無理なら関数化してビューに貼り付ける
"""
