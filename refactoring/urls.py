"""Urls of refactoring app"""

from django.urls import path

from refactoring.views import (
    CodeInputView,
    code_refactoring_view,
    download_recommendations_file_view,
    IndexView,
    RefactoringRulesView,
    SavedRecommendationsView,
    save_recommendations_view,
)


app_name = "refactoring"

urlpatterns = [
    # Code input
    path(
        "code_input/",
        CodeInputView.as_view(),
        name="code_input",
    ),

    # Code refactoring
    path(
        "code_refactoring/",
        code_refactoring_view,
        name="code_refactoring",
    ),

    # Recommendations files downloading
    path(
        "download/<str:file_extention>/",
        download_recommendations_file_view,
        name="download_recommendations_file",
    ),

    # Index
    path(
        "",
        IndexView.as_view(),
        name="index",
    ),

    # Refactoring rules
    path(
        "refactoring_rules/",
        RefactoringRulesView.as_view(),
        name="refactoring_rules",
    ),

    # Saved recommendations
    path(
        "saved_recommendations/",
        SavedRecommendationsView.as_view(),
        name="saved_recommendations",
    ),

    # Recommendations saving
    path(
        "save_recommendations/",
        save_recommendations_view,
        name="save_recommendations",
    ),
]
