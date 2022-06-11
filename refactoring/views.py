"""Views of refactoring app"""

from logging import getLogger
from json import loads

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from django.http.response import HttpResponse
from dicttoxml import dicttoxml

from refactoring.code_inspector import CodeInspector
from refactoring.models import UserRecomendation


class UserRecommendationsListView(LoginRequiredMixin, ListView):
    """User recommendations"""

    template_name = 'user_recommendations.html'

    context_object_name = 'recommendations'

    def get_queryset(self):
        return UserRecomendation.objects.filter(user=self.request.user)


class ManualCodeInputView(TemplateView):
    """View for manual code input"""

    template_name = 'manual_code_input.html'


class IndexView(LoginRequiredMixin, TemplateView):
    """View for index page"""

    template_name = 'index.html'


class InstructionView(LoginRequiredMixin, TemplateView):
    """View for instruction page"""

    template_name = 'instruction.html'


class RulesView(LoginRequiredMixin, TemplateView):
    """View for rules page"""

    template_name = 'rules.html'


class RefactoringResultsView(LoginRequiredMixin, TemplateView):
    """View for refactoring results page"""

    template_name = 'refactoring_results.html'


@login_required()
def refactor_code_handler(request: WSGIRequest) -> HttpResponse:
    """Handler for code refactoring"""

    try:
        code = request.POST['code']

        code_inspector = CodeInspector(code)
        code_errors = code_inspector.errors

        for key, value in code_errors.items():
            code_errors[key] = ", ".join(value)

        if len(code_errors) == 0:
            code_errors = 'Ваш код чистый!'
    except Exception as error:
        getLogger().error(f'Error: {error}')
        code_errors = {}

    return render(
        request,
        'refactoring_results.html',
        {
            'results': code_errors,
            'code': code,
        },
    )


@login_required()
def save_recomendations(request: WSGIRequest) -> JsonResponse:
    """Save refactoring recomendations for the user"""

    recomendation = request.GET.get('recomendation', None)
    code = request.GET.get('code', None)
    user_login = request.GET.get('user', None)

    if recomendation and code and user_login:
        UserRecomendation.objects.create(
            user=get_user_model().objects.get(username=user_login),
            code=code,
            recomendation=recomendation,
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
