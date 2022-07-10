"""Urls of refactoring app"""

from django.urls import path

from refactoring.views import (
    CodeInputView, IndexView, InstructionView, RulesView, refactor_code,
    RefactoringRecommendationListView, download_recommendations_in_json,
    download_results_in_pdf, save_recommendation, download_results_in_xml,
)


app_name = 'refactoring'

urlpatterns = [
    # Index page
    path(
        '',
        IndexView.as_view(),
        name='index',
    ),

    # Code input

    path(
        'code_input/',
        CodeInputView.as_view(),
        name='code_input',
    ),

    # Saved recommendations

    path(
        'saved_recommendations/',
        RefactoringRecommendationListView.as_view(),
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
        'code_refactoring/',
        refactor_code,
        name='code_refactoring',
    ),

    # Recommendations downloading

    path(
        'download_json/',
        download_recommendations_in_json,
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
        'save_recommendation/',
        save_recommendation,
        name='save_recommendation',
    ),
]
