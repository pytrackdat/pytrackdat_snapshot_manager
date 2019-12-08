import os
import shutil
from datetime import datetime

from django.conf import settings
from django.db import models, transaction
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.http import HttpResponse, Http404


class Snapshot(models.Model):
    pdt_created_at = models.DateTimeField(auto_now_add=True, null=False)
    pdt_modified_at = models.DateTimeField(auto_now=True, null=False)
    snapshot_type = models.TextField(help_text="Created by whom?", max_length=6, default='manual',
                                     choices=(("auto", "Automatic"), ("manual", "Manual")), null=False, blank=False)
    name = models.TextField(help_text="Name of snapshot file", max_length=127, null=False, blank=False)
    reason = models.TextField(help_text="Reason for snapshot creation", max_length=127, null=False, blank=True,
                              default="Manually created")
    size = models.IntegerField(help_text="Size of database (in bytes)", null=False)

    def __str__(self):
        return "{} snapshot ({}; size: {} bytes)".format(self.snapshot_type, str(self.name), str(self.size))

    def save(self, *args, **kwargs):
        if not self.pk:
            with transaction.atomic():
                # TODO: THIS ONLY WORKS WITH SQLITE
                # Newly-created snapshot

                name = "snapshot-{}.sqlite3".format(str(datetime.utcnow()).replace(" ", "_").replace(":", "-"))

                shutil.copyfile(settings.DATABASES["default"]["NAME"],
                                os.path.join(settings.BASE_DIR, "snapshots", name))

                self.name = name
                self.size = os.path.getsize(os.path.join(settings.BASE_DIR, "snapshots", name))

        super(Snapshot, self).save(*args, **kwargs)


@receiver(pre_delete, sender=Snapshot)
def delete_snapshot_file(sender, instance, **kwargs):
    try:
        os.remove(os.path.join(settings.BASE_DIR, "snapshots", instance.name))
    except OSError:
        print("Error deleting snapshot")
        # TODO: prevent deletion in some way?
