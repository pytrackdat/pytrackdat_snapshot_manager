from . import views

urls = [
    path("snapshots/<int:snapshot_id>/download/", views.download_view, name="snapshot-download"),
]
