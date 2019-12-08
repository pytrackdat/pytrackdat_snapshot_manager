import os

from django.conf import settings
from django.contrib.auth.decorators import login_required

from .models import Snapshot


@login_required
def download_view(request, snapshot_id):
    try:
        snapshot = Snapshot.objects.get(pk=snapshot_id)
        path = os.path.join(settings.BASE_DIR, "snapshots", snapshot.name)
        if os.path.exists(path):
            # TODO
            with open(path, "rb") as f:
                response = HttpResponse(f.read(), content_type="application/x-sqlite3")
                response["Content-Disposition"] = "inline; filename={}".format(snapshot.name)
                return response
        else:
            raise Http404("Snapshot file does not exist (database inconsistency!)")

    except Snapshot.DoesNotExist:
        raise Http404("Snapshot does not exist")
