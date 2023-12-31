# Generated by Django 4.2.6 on 2023-10-22 02:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='이메일')),
                ('password', models.CharField(verbose_name='비밀번호')),
                ('payment_status', models.IntegerField(choices=[(0, '무료'), (1, '프로'), (2, '프로플러스'), (3, '엔터프라이즈')], default=0, verbose_name='결제 상태')),
                ('registered_date', models.DateTimeField(auto_now=True, verbose_name='가입일')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '유저',
                'verbose_name_plural': '유저 목록',
            },
        ),
        migrations.CreateModel(
            name='AIModel',
            fields=[
                ('model_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='모델 id')),
                ('model_name', models.CharField(max_length=50, verbose_name='모델 이름')),
                ('create_date', models.DateTimeField(null=True, verbose_name='생성일')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='유저 id')),
            ],
            options={
                'verbose_name': 'AI모델',
                'verbose_name_plural': 'AI모델 목록',
            },
        ),
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_message', models.CharField(default='대화를 시작해보세요!', verbose_name='마지막 메세지')),
                ('model_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='omg_app.aimodel', verbose_name='모델 id')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='유저 id')),
            ],
            options={
                'verbose_name': '채팅방',
                'verbose_name_plural': '채팅방 목록',
            },
        ),
        migrations.CreateModel(
            name='SubscriptionProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(verbose_name='상품명')),
                ('amount', models.IntegerField(default=0, verbose_name='상품 가격')),
            ],
            options={
                'verbose_name': '상품',
                'verbose_name_plural': '상품 목록',
            },
        ),
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='게시일')),
                ('views', models.IntegerField(default=0, verbose_name='조회수')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='유저 아이디')),
            ],
            options={
                'verbose_name': '포스팅',
                'verbose_name_plural': '포스팅 목록',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_id', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='가맹점 코드')),
                ('amount', models.PositiveIntegerField(default=100, verbose_name='결제 금액')),
                ('payment_date', models.DateTimeField(auto_now_add=True, verbose_name='결제 갱신일')),
                ('payment_type', models.CharField(choices=[('card', '신용카드')], default='card', max_length=10, verbose_name='결제 수단')),
                ('status', models.CharField(choices=[('await', '결제대기'), ('paid', '결제성공'), ('failed', '결제실패'), ('cancelled', '결제취소')], default='await', max_length=10, verbose_name='결제상태')),
                ('subscription_product_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='omg_app.subscriptionproduct', verbose_name='상품ID')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='유저 id')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='메세지')),
                ('send_date', models.DateTimeField(auto_now=True, verbose_name='발송일시')),
                ('is_user', models.BooleanField(default=True, verbose_name='사용자가 보낸 메세지 인지')),
                ('chat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='omg_app.chatroom', verbose_name='채팅방 id')),
                ('sender_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='채팅방 id')),
            ],
            options={
                'verbose_name': '채팅 메세지',
                'verbose_name_plural': '채팅 메세지 목록',
            },
        ),
    ]
