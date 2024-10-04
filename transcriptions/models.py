# final_project/transcriptions/models.py


from django.db import models

class Transcription(models.Model):
    CALLER_ID_MAX_LENGTH = 255
    SENTIMENT_CHOICES = [
        ('Positive', 'Positive'),
        ('Negative', 'Negative'),
        ('Neutral', 'Neutral'),  # Optional: If you want to add a Neutral option
    ]
    caller_id = models.CharField(max_length=CALLER_ID_MAX_LENGTH)
    agent_transcription = models.TextField(null=True, blank=True)
    agent_translation = models.TextField(null=True, blank=True)
    customer_transcription = models.TextField(null=True, blank=True)
    customer_translation = models.TextField(null=True, blank=True)
    agent_sentiment_score = models.CharField(max_length=10, choices=SENTIMENT_CHOICES, null=True, blank=True)
    customer_sentiment_score = models.CharField(max_length=10, choices=SENTIMENT_CHOICES, null=True, blank=True)

    class Meta:
        db_table = 'transcriptions'  # Make sure this matches the actual table name
