from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


#回答者フォーム、質問者フォームをimportする。

from faq.forms import QuestionUserForm,AnswerUserForm

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model   = CustomUser
        fields  = ("username","email","first_name","last_name")


    #TODO:ここに回答者、質問者のモデルにそれぞれ追加情報を記録する(saveメソッドのオーバーライドで)
    #https://noauto-nolife.com/post/django-models-save-delete-override/

    #下記でも会員登録時に追加の処理ができる。(カスタムユーザーモデルを使用していない場合専用？)
    #https://django-allauth.readthedocs.io/en/latest/forms.html#signup-allauth-account-forms-signupform


    #TODO:ここで追加のフォームの保存もするため、requestを引数として受ける。argsで受け取っても良いが混乱するので。
    def save(self, request, *args, **kwargs):

        #ココでユーザーモデルに記録。記録したユーザーのidを取得するため、返り値のユーザーモデルのオブジェクトを手に入れる。
        user    = super().save(*args, **kwargs)


        #以降、質問者・回答者の追加情報を記録
        copied          = request.POST.copy()
        copied["user"]  = user.id
        
        question_form   = QuestionUserForm(copied)

        #バリデーションOKになるには、userとseriousnessがモデルで定義したルールに則っていればよい。それ以外に余計なものが入っていたとしてもNGにはならない(除外されるだけ)
        if question_form.is_valid():
            print("質問者ユーザー登録")
            question_form.save()
        else:
            print("質問者ユーザーではない")

        answer_form     = AnswerUserForm(copied)

        if answer_form.is_valid():
            print("回答者ユーザー登録")
            answer_form.save()
        else:
            print("回答者ユーザーではない")


    #TODO:リダイレクト先にパラメータを含ませるため、ここでis_valid()のオーバーライドをする。



