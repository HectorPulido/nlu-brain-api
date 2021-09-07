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

    data = models.CharField(max_length=500)

    record_index = models.CharField(max_length=500, db_index=True)

    record_type = models.CharField(
        max_length=2,
        choices=RecordType.choices,
        default=RecordType.RESOURCE,
        db_index=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

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
