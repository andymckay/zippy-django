from django.db import models

STATUS_ACTIVE = 0
STATUS_INACTIVE = 1
STATUS_DISABLED = 2

STATUSES = (
    (STATUS_ACTIVE, 'ACTIVE'),
    (STATUS_INACTIVE, 'INACTIVE'),
    (STATUS_DISABLED, 'DISABLED')
)


class Seller(models.Model):
    agreement = models.DateTimeField(blank=True, null=True)
    email = models.EmailField()
    name = models.CharField(max_length=255)
    status = models.IntegerField(default=STATUS_ACTIVE, choices=STATUSES)
    uuid = models.CharField(max_length=255)

    class Meta:
        db_table = 'seller'
