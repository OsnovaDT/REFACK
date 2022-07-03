"""Initial migration that create RefactoringRecommendation model"""

from django.conf import settings
from django.db import migrations, models
from django.db.models.deletion import CASCADE


class Migration(migrations.Migration):
    """Migration"""

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RefactoringRecommendation',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    )
                ),
                ('code', models.TextField(max_length=10000)),
                ('recommendation', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    )
                ),
            ],
            options={
                'verbose_name': 'Рекомендация по рефакторингу',
                'verbose_name_plural': 'Рекомендации по рефакторингу',
                'ordering': ['-date'],
            },
        ),
    ]
