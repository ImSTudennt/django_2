# Generated by Django 4.1 on 2023-03-02 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_remove_student_teacher_student_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
        migrations.AddField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='students', to='school.teacher'),
        ),
    ]
