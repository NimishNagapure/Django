
from core.models import CheckList, CheckListItem
from django.urls import path,include
from .views import CheckListsAPIView,CheckListAPIView, ChecklistItemAPIView, ChecklistItemCreateAPIView

urlpatterns = [
    path('auth/', include('rest_framework_social_oauth2.urls')),
    path('api/checklists/',CheckListsAPIView.as_view()),
    path('api/checklist/<int:pk>',CheckListAPIView.as_view()),
    path('api/checklistitem/create/',ChecklistItemCreateAPIView.as_view()),
    path('api/checklistitem/<int:pk>',ChecklistItemAPIView.as_view())


]
