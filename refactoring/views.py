"""Views of refactoring app"""

from json import loads

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.handlers.wsgi import WSGIRequest
from django.http import FileResponse, JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from dicttoxml import dicttoxml

from refactoring.models import RefactoringRecommendation
from refactoring.services import (
    get_code_recommendations, get_recommendations_or_error_response,
    get_code_to_display_in_html, get_recommendation_to_display_in_html,
    get_str_for_deserialization,
)
from refactoring.constants import FILE_DEFAULT_DISPOSITION


# Code input


class ManualCodeInputView(TemplateView):
    """Manual code input"""

    template_name = 'code_input/manual.html'


class FileCodeInputView(TemplateView):
    """File code input"""

    template_name = 'code_input/file.html'


# Index, instruction and rules pages


class IndexView(LoginRequiredMixin, TemplateView):
    """Index page"""

    template_name = 'index.html'


class InstructionView(LoginRequiredMixin, TemplateView):
    """Instruction page"""

    template_name = 'navbar/instruction.html'


class RulesView(LoginRequiredMixin, TemplateView):
    """Rules page"""

    template_name = 'navbar/rules.html'


# Refactoring


@login_required()
def refactor_code_from_file(request: WSGIRequest) -> HttpResponse:
    """Refactor code from file"""

    code = request.FILES['file_upload'].read().decode('UTF-8')

    return render(
        request,
        'refactoring_results.html',
        {
            'results': get_code_recommendations(code),
            'code': code,
        },
    )


@login_required()
def refactor_code(request: WSGIRequest) -> JsonResponse:
    """Refactor code and return recommendations or error"""

    code = request.GET.get('code', '')

    return get_recommendations_or_error_response(code)


# Refactoring recommendations


class RefactoringRecommendationListView(LoginRequiredMixin, ListView):
    """Refactoring recommendations owned by the user"""

    template_name = 'saved_recommendations.html'

    context_object_name = 'recommendations'

    def get_queryset(self):
        return RefactoringRecommendation.objects.filter(
            user=self.request.user,
        )


@login_required()
def save_recommendation(request: WSGIRequest) -> JsonResponse:
    """Save refactoring recommendation for the user"""

    recommendation = request.GET.get('recommendation', None)

    code = request.GET.get('code', None)

    user_login = request.GET.get('user', None)

    if recommendation and code and user_login:
        RefactoringRecommendation.objects.create(
            user=get_user_model().objects.get(username=user_login),
            code=get_code_to_display_in_html(code),
            recommendation=get_recommendation_to_display_in_html(
                recommendation,
            ),
        )

    return JsonResponse({})


@login_required()
def download_recommendations_in_json(request: WSGIRequest) -> JsonResponse:
    """Download JSON file with refactoring recommendations"""

    recommendations = get_str_for_deserialization(request.POST['results'])

    response = JsonResponse(
        loads(recommendations),
        json_dumps_params={'ensure_ascii': False},
    )
    response['Content-Disposition'] = FILE_DEFAULT_DISPOSITION + 'json;'

    return response


@login_required()
def download_results_in_pdf(request: WSGIRequest) -> FileResponse:
    """Download PDF file with refactoring recommendations"""

    response = FileResponse(
        request.POST['results'],
        content_type='application/pdf',
    )

    response['Content-Disposition'] = FILE_DEFAULT_DISPOSITION + 'pdf;'

    return response


@login_required()
def download_results_in_xml(request: WSGIRequest) -> FileResponse:
    """Download XML file with refactoring recommendations"""

    recommendations = request.POST['results']
    recommendations = loads(get_str_for_deserialization(recommendations))

    response = FileResponse(
        str(dicttoxml(recommendations)),
        content_type='application/xml',
    )

    response['Content-Disposition'] = FILE_DEFAULT_DISPOSITION + 'xml;'

    return response
