"""Views of refactoring app"""

from json import loads

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from dicttoxml import dicttoxml

from refactoring.models import RefactoringRecommendation
from refactoring.services.utils import (
    get_code_recommendations, get_recommendations_or_error_response,
)


class SavedRecommendationsListView(LoginRequiredMixin, ListView):
    """User's saved recommendations"""

    template_name = 'saved_recommendations.html'

    context_object_name = 'recommendations'

    def get_queryset(self):
        return RefactoringRecommendation.objects.filter(user=self.request.user)


class ManualCodeInputView(TemplateView):
    """View for manual code input"""

    template_name = 'manual_code_input.html'


class FileCodeInputView(TemplateView):
    """View for file code input"""

    template_name = 'file_code_input.html'


class IndexView(LoginRequiredMixin, TemplateView):
    """View for index page"""

    template_name = 'index.html'


class InstructionView(LoginRequiredMixin, TemplateView):
    """View for instruction page"""

    template_name = 'instruction.html'


class RulesView(LoginRequiredMixin, TemplateView):
    """View for rules page"""

    template_name = 'rules.html'


@login_required()
def refactor_code_from_file(request: WSGIRequest):
    """Refactor code from file"""

    code = request.FILES['code_upload'].read().decode('UTF-8')

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
    """Refactor code and return recommendations"""

    code = request.GET.get('code', '')

    return get_recommendations_or_error_response(code)


@login_required()
def save_recommendations(request: WSGIRequest) -> JsonResponse:
    """Save refactoring recommendations for the user"""

    recommendation = request.GET.get('recommendation', None)
    code = request.GET.get('code', None)
    user_login = request.GET.get('user', None)

    if recommendation and code and user_login:
        RefactoringRecommendation.objects.create(
            user=get_user_model().objects.get(username=user_login),
            code=code.replace('\n', '<br>').replace(' ', '&nbsp;'),
            recommendation=recommendation.replace(', ', '<br><br>')
            .replace('{', '')
            .replace('}', '')
            .replace("'", ''),
        )

    return JsonResponse({})


@login_required()
def download_results_in_json(request: WSGIRequest):
    """Handler for downloading JSON file with refactoring results"""

    results = request.POST['results']
    results = results.replace('\'', '\"')

    response = JsonResponse(
        loads(results),
        json_dumps_params={'ensure_ascii': False},
    )
    response['Content-Disposition'] = \
        'attachment; filename=refactoring_results.json;'

    return response


@login_required()
def download_results_in_pdf(request: WSGIRequest):
    """Handler for downloading PDF file with refactoring results"""

    response = FileResponse(
        request.POST['results'],
        content_type='application/pdf',
    )
    response['Content-Disposition'] = \
        'attachment; filename=refactoring_results.pdf;'

    return response


@login_required()
def download_results_in_xml(request: WSGIRequest):
    """Handler for downloading XML file with refactoring results"""

    results = request.POST['results']
    results = loads(results.replace('\'', '\"'))

    response = FileResponse(
        str(dicttoxml(results)),
        content_type='application/xml',
    )
    response['Content-Disposition'] = \
        'attachment; filename=refactoring_results.xml;'

    return response
