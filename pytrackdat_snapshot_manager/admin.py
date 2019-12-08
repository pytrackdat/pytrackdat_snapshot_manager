from django.contrib import admin
from django.utils.html import format_html

from snapshot_manager.models import *


@admin.register(Snapshot)
class SnapshotAdmin(admin.ModelAdmin):
    exclude = ('snapshot_type', 'size', 'name', 'reason')
    list_display = ('__str__', 'download_link', 'reason')

    def download_link(self, obj):
        return format_html('<a href="{url}">Download Database Snapshot</a>',
                           url='/snapshots/{}/download/'.format(obj.pk))

    download_link.short_description = 'Download Link'
