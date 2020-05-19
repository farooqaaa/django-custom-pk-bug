from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class EmailAddress(models.Model):
    address = models.EmailField(primary_key=True)
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='emails',
        related_query_name='email',
    )
    
    def delete(self, using=None, keep_parents=False):
        """Preserve PK before deleting"""
        self._pk = self.pk
        super().delete(using, keep_parents)

    def __str__(self):
        """
        Because `address` is set to `None` when an `EmailAddress` is being deleted,
        this function returns `None` when the admin app tries to write a change log.
        """
        return getattr(self, '_pk', self.pk)
