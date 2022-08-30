"""Views of refactoring app"""

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.handlers.wsgi import WSGIRequest
from django.http import FileResponse, JsonResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from refactoring.models import RefactoringRecommendation
from refactoring.services import (
    create_refactoring_recommendation,
    get_file_with_refactoring_recommendations,
    get_recommendations_or_error_response,
)


class CodeInputView(LoginRequiredMixin, TemplateView):
    """Code input page"""

    template_name = "code_input.html"


class IndexView(LoginRequiredMixin, TemplateView):
    """Index page"""

    template_name = "index.html"


class RefactoringRulesView(LoginRequiredMixin, TemplateView):
    """Refactoring rules page"""

    template_name = "rules.html"


# Code refactoring


@login_required
def code_refactoring_view(request: WSGIRequest) -> JsonResponse:
    """Refactor the code and return recommendations or error"""

    code = request.GET.get("code", "")

    return get_recommendations_or_error_response(code)


# Refactoring recommendations


class SavedRecommendationsView(LoginRequiredMixin, ListView):
    """Refactoring recommendations saved by the user"""

    template_name = "saved_recommendations.html"

    context_object_name = "recommendations"

    def get_queryset(self):
        return RefactoringRecommendation.objects.filter(
            user=self.request.user,
        )


@login_required
def save_recommendations_view(request: WSGIRequest) -> JsonResponse:
    """Save refactoring recommendation for the user"""

    code = request.GET.get("code", None)
    recommendation = request.GET.get("recommendation", None)

    if code and recommendation:
        create_refactoring_recommendation({
            "code": code,
            "recommendation": recommendation,
            "username": request.user,
        })

    return JsonResponse({})


@login_required
def download_recommendations_file_view(
        request: WSGIRequest,
        file_extention: str) -> FileResponse | JsonResponse:
    """Download file with refactoring recommendations"""

    return get_file_with_refactoring_recommendations(
        request.POST["results"],
        file_extention,
    )
