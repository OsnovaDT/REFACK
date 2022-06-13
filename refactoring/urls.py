"""Urls of refactoring app"""

from django.urls import path

from refactoring.views import (
    ManualCodeInputView, IndexView, refactor_code_handler,
    RefactoringResultsView, InstructionView, RulesView,
    download_results_in_json, download_results_in_pdf, FileCodeInputView,
    download_results_in_xml, save_recomendations, UserRecommendationsListView,
    refactoring_code_from_file,
)


app_name = 'refactoring'

urlpatterns = [
    path(
        '',
        IndexView.as_view(),
        name='index',
    ),

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

    path(
        'refactoring_for_file/',
        refactoring_code_from_file,
        name='refactoring_for_file',
    ),

    path(
        'refactor/',
        refactor_code_handler,
        name='refactor',
    ),

    path(
        'results/',
        RefactoringResultsView.as_view(),
        name='results',
    ),

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

    path(
        'json_download/',
        download_results_in_json,
        name='json_download',
    ),

    path(
        'pdf_download/',
        download_results_in_pdf,
        name='pdf_download',
    ),

    path(
        'xml_download/',
        download_results_in_xml,
        name='xml_download',
    ),

    path(
        'save_recomendations/',
        save_recomendations,
        name='save_recomendations',
    ),

    path(
        'user_recommendations/',
        UserRecommendationsListView.as_view(),
        name='user_recommendations',
    ),
]
