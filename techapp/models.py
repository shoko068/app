from django.conf import settings
#ここから追加分ユーザーを拡張するモデルを作る
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_l = models.CharField("業態カテゴリ", max_length=10, blank=False)
    name = models.CharField("業態名", max_length=30, blank=False)

    def __str__(self):
        return str(self.name)

class Pref(models.Model):
    pref = models.CharField("都道府県コード", max_length=6, blank=False)
    name = models.CharField("都道府県名", max_length=10, blank=False)

    def __str__(self):
        return str(self.name)

BABYCAR_CHOICES = [
    [0, "ベビーカー入店不可"],
    [1, "ベビーカー入店可能"]
    ]

BABYCHAIR_CHOICES = [
    (0, "ベビーチェア有り"),
    (1, "ベビーチェア無し")
    ]

SOFA_CHOICES = [
    (0, "ソファー席無し"),
    (1, "ソファー席有り")
    ]

KIDS_MENU_CHOICES = [
    (0, "キッズメニュー無し"),
    (1, "キッズメニュー有り")
]

DIAPER_CHOICES = [
    (0, "おむつ交換台無し"),
    (1, "おむつ交換台有り"),
]

BABYFOOD_CHOICES = [
    (0, "離乳食持ち込み不可"),
    (1, "離乳食持ち込み可能")
]

class Review(models.Model):
    shop_id = models.CharField('店舗ID', max_length=10, blank=False)
    shop_name = models.CharField('店舗名', max_length=200, blank=False)
    image_url = models.CharField('画像１URL', max_length=300, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    comment = models.TextField(verbose_name='レビューコメント', blank=False)
    babycar_info = models.PositiveSmallIntegerField(verbose_name='ベビーカー情報',choices=BABYCAR_CHOICES,default='0')
    babychair_info = models.PositiveSmallIntegerField(verbose_name='ベビーチェア情報',choices=BABYCHAIR_CHOICES,default='0')
    sofa_info = models.PositiveSmallIntegerField(verbose_name='ソファー席情報',choices=SOFA_CHOICES,default='0')
    kids_menu_info = models.PositiveSmallIntegerField(verbose_name='キッズメニュー情報',choices=KIDS_MENU_CHOICES,default='0')
    diaper_info = models.PositiveSmallIntegerField(verbose_name='おむつ交換台情報',choices=DIAPER_CHOICES,default='0')
    babyfood_info = models.PositiveSmallIntegerField(verbose_name='離乳食情報',choices=BABYFOOD_CHOICES,default='0')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('shop_id', 'user')
        db_table = 'Reviews'

    def __str__(self):
        return str(self.shop_id)

class Tag(models.Model):
    name = models.CharField('タグ名', max_length=100)

    def __str__(self):
        return self.name
# Create your models here.

#追加
class Profile(models.Model):
    name=models.CharField("ニックネーム",max_length=255)
    email=models.CharField("メールアドレス",max_length=255)
    password=models.CharField("パスワード",max_length=8)
    kids_age=models.CharField("子供の年代",max_length=8)
    user_register_date=models.TimeField("顧客情報登録日",max_length=255)
    user_update_date=models.TimeField("顧客情報更新日",max_length=255)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,null=True)

#ここは必要ないかも
    def __str__(self):
        return self.name
"""
class Shop_Info(models.Model):
    shop_id=models.CharField("店舗ID",max_length=4)
    shop_name=models.CharField("店舗名",max_length=255)
    address=models.CharField("店舗住所",max_length=255)
    phone=models.CharField("電話番号",max_length=4)
    postcode=models.CharField("郵便番号",max_length=4)
    shop_register_date=models.TimeField("登録日")
    shop_update_date=models.TimeField("更新日")
    #地図のモデルがわからない
    map=models.URLField("地図")
    shop_customer_comment=models.CharField("顧客コメント")
    shop_customer_evaluation1=models.CharField("ベビーカーOK")
    shop_customer_evaluation2=models.CharField("離乳食持ち込みOK")
    shop_customer_evaluation3=models.CharField("ベビーチェア有")
    shop_customer_evaluation4=models.CharField("ソファ席有")
    shop_customer_evaluation5=models.CharField("おむつ交換台あり")

class ShopInfoForm(forms.ModelForm):
    class Meta:
        model = ShopForm
        fields = (
        "shop_id" , "shop_name", "address", "phone", "postcode", "map", "shop_register_date", "shop_update_date", "map",
        "shop_custoer_comment"
        "shop_customer_evaluation1", "shop_customer_evaluation2", "shop_customer_evaluation3", "shop_customer_evaluation4", "shop_customer_evaluation5",
        )

class Comment(models.Model):
    customer_id=models.CharField("顧客番号",max_length=4)
    customer_comment=models.CharField("顧客コメント",max_length=255)
    user_id=models.CharField("顧客ID",max_length=4)
    shop_id=models.CharField("店舗ID",max_length=4)
    customer_evaluation1=models.CharField("ベビーカーOK")
    customer_evaluation2=models.CharField("離乳食持ち込みOK")
    customer_evaluation3=models.CharField("ベビーチェア有")
    customer_evaluation4=models.CharField("ソファ席有")
    customer_evaluation5=models.CharField("おむつ交換台あり")
    comment_create_date=models.TimeField("コメント登録日")
    comment_update_date=models.TImeField("コメント更新日")

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentForm
        fields = (
        "customer_id", "customer_comment", "user_id", "shop_id", "customer_evaluation1", "customer_evaluation2", "customer_evaluation3", "customer_evaluation4", "customer_evaluation5"
        "comment_create_date", "comment_update_date"
        )
"""
