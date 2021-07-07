# Generated by Django 3.2.4 on 2021-07-07 22:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bucket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('name', models.CharField(max_length=140, verbose_name='Bucket name')),
                ('slug_name', models.SlugField(max_length=40, unique=True)),
                ('description', models.CharField(max_length=255, verbose_name='Bucket description')),
                ('is_public', models.BooleanField(default=True, help_text='Public buckets are listed in the main page so everyone know about their existence.')),
                ('is_limited', models.BooleanField(default=False, help_text='Limited buckets can grow up to a fixed number of members.', verbose_name='Is limited')),
                ('members_limit', models.PositiveIntegerField(default=0, help_text='If a bucket is limited, this will be the limit on the number of members.', verbose_name='Members limit')),
                ('bucket_size', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['-bucket_size'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('is_admin', models.BooleanField(default=False, help_text="Bucket admins can update the bucket's data and manage its members.", verbose_name='bucket admin')),
                ('used_invitations', models.PositiveSmallIntegerField(default=0)),
                ('remaining_invitations', models.PositiveSmallIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True, help_text='Only active users are allowed to interact in the bucket.', verbose_name='active status')),
                ('bucket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buckets.bucket')),
                ('invited_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invited_by', to=settings.AUTH_USER_MODEL)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='bucket',
            name='members',
            field=models.ManyToManyField(through='buckets.Membership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bucket',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
