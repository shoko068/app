# Generated by Django 3.0.7 on 2020-11-04 05:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('techapp', '0005_auto_20200629_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='info',
        ),
        migrations.RemoveField(
            model_name='review',
            name='score',
        ),
        migrations.AddField(
            model_name='review',
            name='babycar_info',
            field=models.PositiveSmallIntegerField(choices=[[0, 'ベビーカー入店不可'], [1, 'ベビーカー入店可能']], default='0', verbose_name='ベビーカー情報AAA'),
        ),
        migrations.AddField(
            model_name='review',
            name='babychair_info',
            field=models.PositiveSmallIntegerField(choices=[(0, 'ベビーチェア無し'), (1, 'ベビーチェア無し')], default='0', verbose_name='ベビーチェア情報'),
        ),
        migrations.AddField(
            model_name='review',
            name='babyfood_info',
            field=models.PositiveSmallIntegerField(choices=[(0, '離乳食持ち込み不可'), (1, '離乳食持ち込み可能')], default='0', verbose_name='離乳食情報'),
        ),
        migrations.AddField(
            model_name='review',
            name='diaper_info',
            field=models.PositiveSmallIntegerField(choices=[(0, 'おむつ交換台無し'), (1, 'おむつ交換台有り')], default='0', verbose_name='おむつ交換台情報'),
        ),
        migrations.AddField(
            model_name='review',
            name='kids_menu_info',
            field=models.PositiveSmallIntegerField(choices=[(0, 'キッズメニュー無し'), (1, 'キッズメニュー有り')], default='0', verbose_name='キッズメニュー情報'),
        ),
        migrations.AddField(
            model_name='review',
            name='sofa_info',
            field=models.PositiveSmallIntegerField(choices=[(0, 'ソファー席無し'), (1, 'ソファー席有り')], default='0', verbose_name='ソファー席情報'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ニックネーム')),
                ('email', models.CharField(max_length=255, verbose_name='メールアドレス')),
                ('password', models.CharField(max_length=8, verbose_name='パスワード')),
                ('kids_age', models.CharField(max_length=8, verbose_name='子供の年代')),
                ('user_register_date', models.TimeField(max_length=255, verbose_name='顧客情報登録日')),
                ('user_update_date', models.TimeField(max_length=255, verbose_name='顧客情報更新日')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]