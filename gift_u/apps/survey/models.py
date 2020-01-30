from django.db import models

from django.conf import settings
# Create your models here.

class Questionnaire(models.Model):
    def __str__(self):
        return self.title
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    title = models.CharField(max_length=200, default='匿名信件')

    # 某個人寄得第n封信
    
    # 1.收禮者的email
    receiver_email = models.EmailField(verbose_name="收禮者的email", max_length=254, default='')

    # 2.收禮者的暱稱
    receiver_nickname = models.CharField(verbose_name="收禮者的暱稱", max_length=200, default='')

    # 3.要讓他/她挑選哪三樣禮物呢？


    # 透露一些你的資訊給他/她吧！
    sender_nickname = models.CharField(verbose_name="送禮者的暱稱", max_length=200, default='')

    # Todo:認識對方多久了呢？（年/月/週）
    YEAR_TYPE = 0
    MONTH_TYPE = 1
    WEEK_TYPE = 2
    type = models.SmallIntegerField(verbose_name="認識多久", choices=( (YEAR_TYPE, '年'), (MONTH_TYPE, '月'),  (WEEK_TYPE, '週') ), default=0, blank=True, null=True)


    # 還想對他/她說些什麼嗎？
    extra_messages = models.CharField(verbose_name="額外想對他/她說的話", max_length=200, default='', blank=True)

    
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, default=1)
    ## 
    # Todo: One Questionnaire...
    # - should be sent to one reciever (also an User).(but it might not yet registered!)
    ##
    # receiver = models.OneToOneField(User, on_delete=models.CASCADE)


# Abstract class! (Only for inheritance)
class Question(models.Model):
    def __str__(self):
        return self.question + ' (' +  '寄件者：' + self.questionnaire.sender_nickname + ')'
    # Relation: 一份問卷有多個問題
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)

    # Property 
    question = models.CharField(max_length=200, verbose_name="問題", default="要讓他/她挑選哪三樣禮物呢？")
    required = models.BooleanField(default=True, help_text="這個問題是否必須回答")
    
    # 在問卷列表中的順序,從1開始
    order_in_list = models.IntegerField(default=1)
    # created_at = models.DateTimeField(auto_now_add=True, editable=False)
    class Meta:
        abstract = True
class ChoiceQuestion(Question):
    """選擇題"""
    # Todo:希望呈現這個問題的三個選項
    # def __str__(self):
    #     return self.choice_text
    multi_choice = models.BooleanField(default=False, verbose_name="是否為多選")

class Choice(models.Model):
    """選擇題的選項"""
    def __str__(self):
        return str(self.order_in_list) + '.' + self.choice_text
    choice_question = models.ForeignKey(ChoiceQuestion, on_delete=models.CASCADE, default=3)
    choice_text = models.CharField(max_length=50, verbose_name="選項")
    order_in_list = models.IntegerField(default=1)

## Todo!!!! 
## 未來如果需要新的功能：使用者可以自己客製化問卷，可以改用這種方式
##

# class NonChoiceQuestion(Question):
#     """填空題"""
#     TEXT_QUESTION_TYPE = 0
#     FILE_QUESTION_TYPE = 1
#     type = models.SmallIntegerField(verbose_name="主觀題型別", choices=( (TEXT_QUESTION_TYPE, '問答題'), (FILE_QUESTION_TYPE, '檔案題') ), default=0)
    
    


