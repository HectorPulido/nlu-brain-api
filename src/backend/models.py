import hashlib
from django.db import models


class UnresolvedQuestions(models.Model):
    question = models.TextField()

    def __str__(self):
        return self.question


class Key(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    enabled = models.BooleanField(default=False)
    private_key = models.TextField()

    def __str__(self):
        return self.name

    @staticmethod
    def get_key_data(name):
        wh = Key.objects.filter(name=name, enabled=True)
        if not wh.exists():
            return ""
        wh = wh.first()
        return wh.private_key


class Record(models.Model):
    class RecordType(models.TextChoices):
        RESOURCE = "RS", "Resource"
        MEME = "ME", "Meme"
        JOB_OFFER = "JO", "Job offer"

    shash = models.CharField(
        max_length=255, unique=True, db_index=True, null=True, blank=True
    )

    data = models.CharField(max_length=500)

    record_index = models.CharField(max_length=500, db_index=True)

    record_type = models.CharField(
        max_length=2,
        choices=RecordType.choices,
        default=RecordType.RESOURCE,
        db_index=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, **kwargs):
        self.data = self.data.strip()
        self.record_index = self.record_index.lower().strip()
        self.shash = hashlib.md5(self.data.encode()).hexdigest()
        if Record.objects.filter(shash=self.shash).exists():
            return None
        super().save(**kwargs)

    def __str__(self):
        return self.data

    @staticmethod
    def search_record(query, record_type):
        return (
            Record.objects.filter(record_type=record_type, record_index__contains=query)
            .order_by("?")
            .first()
        )

    @staticmethod
    def get_random_record(record_type):
        return Record.objects.filter(record_type=record_type).order_by("?").first()


class ChannelType(models.Model):
    class ChannelType(models.TextChoices):
        RESOURCE = "RS", "Resource channel"
        MEME = "ME", "Meme channel"
        JOB_OFFER = "JO", "Job offers channel"
        EMOJI_ONLY = "EM", "Emoji only channel"

    name = models.CharField(max_length=250)
    channel_id = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=2, choices=ChannelType.choices)

    @classmethod
    def get_all_channels_as_dict(cls):
        return {
            channel.channel_id: channel.type for channel in ChannelType.objects.all()
        }

    def __str__(self):
        return f"{self.name} - {self.type}"
