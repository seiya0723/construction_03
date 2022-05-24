from django.contrib import admin

from .models import Question,Answer,Reply,QuestionUser,AnswerUser


class QuestionAdmin(admin.ModelAdmin):
    list_display    = ["title","dt","content","accept_dt","user",]


class AnswerAdmin(admin.ModelAdmin):
    list_display    = ["dt","content","question","user",]


class ReplyAdmin(admin.ModelAdmin):
    list_display    = ["dt","content","answer","user",]



class AnswerUserAdmin(admin.ModelAdmin):
    list_display    = ["user","user_first_name","user_last_name","company","approval"]
    list_editable   = ["approval"]


    def user_first_name(self,obj):
        return obj.user.first_name

    def user_last_name(self,obj):
        return obj.user.last_name





admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer,AnswerAdmin)
admin.site.register(Reply,ReplyAdmin)

admin.site.register(QuestionUser)
admin.site.register(AnswerUser,AnswerUserAdmin)
