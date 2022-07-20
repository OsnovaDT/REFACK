"""Views of refactoring app"""

from json import loads

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.handlers.wsgi import WSGIRequest
from django.http import FileResponse, JsonResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from dicttoxml import dicttoxml

from refactoring.models import RefactoringRecommendation
from refactoring.services import (
    get_recommendations_or_error_response, get_code_to_display_in_html,
    get_recommendation_to_display_in_html,
)
from refactoring.constants import FILE_DEFAULT_DISPOSITION


# Code input


class CodeInputView(LoginRequiredMixin, TemplateView):
    """Manual code input"""

    template_name = 'code_input.html'


# Index, and rules


class IndexView(LoginRequiredMixin, TemplateView):
    """Index page"""

    template_name = 'index.html'


class RulesView(LoginRequiredMixin, TemplateView):
    """Rules page"""

    template_name = 'rules.html'


# Refactoring


@login_required()
def refactor_code_view(request: WSGIRequest) -> JsonResponse:
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
def save_recommendation_view(request: WSGIRequest) -> JsonResponse:
    """Save refactoring recommendation for the user"""

    recommendation = request.GET.get('recommendation', None)

    code = request.GET.get('code', None)

    if recommendation and code:
        RefactoringRecommendation.objects.create(
            user=get_user_model().objects.get(username=request.user),
            code=get_code_to_display_in_html(code),
            recommendation=get_recommendation_to_display_in_html(
                recommendation,
            ),
        )

    return JsonResponse({})


@login_required()
def download_recommendations_json_view(request: WSGIRequest) -> JsonResponse:
    """Download JSON file with refactoring recommendations"""

    response = JsonResponse(
        loads(request.POST['results']),
        json_dumps_params={'ensure_ascii': False},
    )
    response['Content-Disposition'] = FILE_DEFAULT_DISPOSITION + 'json;'

    return response


@login_required()
def download_recommendations_pdf_view(request: WSGIRequest) -> FileResponse:
    """Download PDF file with refactoring recommendations"""

    response = FileResponse(
        request.POST['results'],
        content_type='application/pdf',
    )

    response['Content-Disposition'] = FILE_DEFAULT_DISPOSITION + 'pdf;'

    return response


@login_required()
def download_recommendations_xml_view(request: WSGIRequest) -> FileResponse:
    """Download XML file with refactoring recommendations"""

    recommendations = loads(request.POST['results'])

    response = FileResponse(
        str(dicttoxml(recommendations)),
        content_type='application/xml',
    )

    response['Content-Disposition'] = FILE_DEFAULT_DISPOSITION + 'xml;'

    return response
