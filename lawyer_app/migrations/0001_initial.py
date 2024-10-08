# Generated by Django 5.1.1 on 2024-09-28 16:33

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.TextField(validators=[django.core.validators.MaxLengthValidator(250)])),
                ('mobile_number', models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator('^\\+\\d{1,3}\\d{9,15}$', message="Format: '+919999999999'. Up to 15 digits allowed.")])),
                ('registered_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('case_id', models.AutoField(primary_key=True, serialize=False)),
                ('case_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lawyer_app.client')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('document_id', models.AutoField(primary_key=True, serialize=False)),
                ('document_type', models.CharField(max_length=100)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lawyer_app.case')),
            ],
        ),
        migrations.CreateModel(
            name='Lawyer',
            fields=[
                ('lawyer_id', models.AutoField(primary_key=True, serialize=False)),
                ('specialization', models.CharField(max_length=100)),
                ('address', models.TextField(validators=[django.core.validators.MaxLengthValidator(250)])),
                ('mobile_number', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator('^\\+\\d{1,3}\\d{9,15}$', message="Phone number must be entered in the format: '+919999999999'. Up to 15 digits allowed.")])),
                ('registered_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lawyer_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='lawyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lawyer_app.lawyer'),
        ),
        migrations.CreateModel(
            name='LegalResearch',
            fields=[
                ('research_id', models.AutoField(primary_key=True, serialize=False)),
                ('research_topic', models.CharField(max_length=200)),
                ('researcher_name', models.CharField(max_length=200)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lawyer_app.case')),
            ],
        ),
    ]
