import hashlib
from django.db import models


class Key(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    enabled = models.BooleanField(default=False)
    private_key = models.TextField()

    def __str__(self):
        return self.name


class Record(models.Model):
    class RecordType(models.TextChoices):
        RESOURCE = "RS", "Resource"
        MEME = "ME", "Meme"
        JOB_OFFER = "JO", "Job offer"

    shash = models.CharField(max_length=255, unique=True, db_index=True, null=True, blank=True)

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
