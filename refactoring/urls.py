"""Urls of refactoring app"""

from django.urls import path

from refactoring.views import (
    ManualCodeInputView, IndexView, InstructionView, RulesView,
    FileCodeInputView, SavedRecommendationsListView, download_results_in_json,
    download_results_in_pdf, save_recommendations, download_results_in_xml,
    refactor_code_from_file, refactor_code,
)


app_name = 'refactoring'

urlpatterns = [
    path(
        '',
        IndexView.as_view(),
        name='index',
    ),

    # Code input

    path(
        'manual_input/',
        ManualCodeInputView.as_view(),
        name='manual_input',
    ),

    path(
        'file_input/',
        FileCodeInputView.as_view(),
        name='file_input',
    ),

    # Saved recommendations

    path(
        'saved_recommendations/',
        SavedRecommendationsListView.as_view(),
        name='saved_recommendations',
    ),

    # Instruction and rules

    path(
        'instruction/',
        InstructionView.as_view(),
        name='instruction',
    ),

    path(
        'rules/',
        RulesView.as_view(),
        name='rules',
    ),

    # Code refactoring

    path(
        'file_refactoring/',
        refactor_code_from_file,
        name='file_refactoring',
    ),

    path(
        'code_refactoring/',
        refactor_code,
        name='code_refactoring',
    ),

    # Recommendations downloading

    path(
        'download_json/',
        download_results_in_json,
        name='download_json',
    ),

    path(
        'download_pdf/',
        download_results_in_pdf,
        name='download_pdf',
    ),

    path(
        'download_xml/',
        download_results_in_xml,
        name='download_xml',
    ),

    # Recommendations saving

    path(
        'save_recommendations/',
        save_recommendations,
        name='save_recommendations',
    ),
]
