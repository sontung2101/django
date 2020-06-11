# Generated by Django 3.0.7 on 2020-06-11 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('created_by', models.IntegerField(blank=True, null=True, verbose_name='Created By')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated At')),
                ('updated_by', models.IntegerField(blank=True, null=True, verbose_name='Updated By')),
                ('is_deleted', models.BooleanField(default=False, null=True, verbose_name='IsDeleted')),
                ('version', models.IntegerField(blank=True, default=1, null=True, verbose_name='Version')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ToDo ID')),
                ('content', models.CharField(max_length=100, verbose_name='Content')),
                ('completed', models.BooleanField(blank=True, default=False, null=True, verbose_name='Completed')),
            ],
            options={
                'verbose_name': 'todo',
                'verbose_name_plural': 'todo',
                'db_table': 'tb_todo',
                'ordering': ['-id'],
            },
        ),
        migrations.AddIndex(
            model_name='todomodel',
            index=models.Index(fields=['is_deleted'], name='tb_todo_is_dele_824629_idx'),
        ),
    ]
