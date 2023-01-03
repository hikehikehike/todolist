from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from todo_list.views import (
    TaskListViews,
    TagsListViews,
    TaskCreationViews,
    TaskUpdateViews,
    TaskDeleteViews,
    complete_undo,
    TagsCreationViews,
    TagsUpdateViews,
    TagsDeleteViews
)

urlpatterns = [
    path("", TaskListViews.as_view(), name="task-list"),
    path("tags/", TagsListViews.as_view(), name="tags-list"),
    path("tags/creation/", TagsCreationViews.as_view(), name="tags-creation"),
    path("tags/<int:pk>/update", TagsUpdateViews.as_view(), name="tags-update"),
    path("tags/<int:pk>/delete", TagsDeleteViews.as_view(), name="tags-delete"),
    path("creation/", TaskCreationViews.as_view(), name="task-creation"),
    path("<int:pk>/update", TaskUpdateViews.as_view(), name="task-update"),
    path("<int:pk>/delete", TaskDeleteViews.as_view(), name="task-delete"),
    path("<int:pk>/complete_undo", complete_undo, name="task-complete-undo")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = "todo_list"
