# Generated by Django 5.1.1 on 2024-10-03 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Transcription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("caller_id", models.CharField(max_length=255)),
                ("agent_transcription", models.TextField(blank=True, null=True)),
                ("agent_translation", models.TextField(blank=True, null=True)),
                ("customer_transcription", models.TextField(blank=True, null=True)),
                ("customer_translation", models.TextField(blank=True, null=True)),
                (
                    "agent_sentiment_score",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Positive", "Positive"),
                            ("Negative", "Negative"),
                            ("Neutral", "Neutral"),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "customer_sentiment_score",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Positive", "Positive"),
                            ("Negative", "Negative"),
                            ("Neutral", "Neutral"),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
            ],
            options={
                "db_table": "transcriptions",
            },
        ),
    ]
