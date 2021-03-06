"""Views of refactoring app"""

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.handlers.wsgi import WSGIRequest
from django.http import FileResponse, JsonResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from refactoring.models import RefactoringRecommendation
from refactoring.services import (
    get_recommendations_or_error_response, create_refactoring_recommendation,
    get_file_response_with_refactoring_recommendations,
)


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
        create_refactoring_recommendation({
            'username': request.user,
            'code': code,
            'recommendation': recommendation,
        })

    return JsonResponse({})


@login_required()
def download_recommendations_json_view(request: WSGIRequest) -> JsonResponse:
    """Download JSON file with refactoring recommendations"""

    return get_file_response_with_refactoring_recommendations(
        request.POST['results'], 'json',
    )


@login_required()
def download_recommendations_pdf_view(request: WSGIRequest) -> FileResponse:
    """Download PDF file with refactoring recommendations"""

    return get_file_response_with_refactoring_recommendations(
        request.POST['results'], 'pdf',
    )


@login_required()
def download_recommendations_xml_view(request: WSGIRequest) -> FileResponse:
    """Download XML file with refactoring recommendations"""

    return get_file_response_with_refactoring_recommendations(
        request.POST['results'], 'xml',
    )
