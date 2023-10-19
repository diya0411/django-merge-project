# Generated by Django 4.1.6 on 2023-02-23 10:33

import autoslug.fields
import ckeditor_uploader.fields
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
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
                ('number', models.IntegerField(default=5000000000, validators=[django.core.validators.MinValueValidator(5000000000), django.core.validators.MaxValueValidator(999999999999)])),
                ('company', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=20)),
                ('about', models.TextField(max_length=300)),
                ('image', models.ImageField(upload_to='user_image')),
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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='name', unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='cat_image')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='tag_image')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='name', unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=200, null=True, populate_from='title', unique=True)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField()),
                ('thumbnail', models.ImageField(upload_to='thumbnail_image')),
                ('featured', models.ImageField(upload_to='feature_image')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='blog_category', to='blog.category')),
                ('tag', models.ManyToManyField(blank=True, to='blog.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('comment', models.CharField(max_length=50)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='replies', to='blog.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='blog.post')),
            ],
        ),
    ]