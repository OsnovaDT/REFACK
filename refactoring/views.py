"""Views of refactoring app"""

from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse


class ManualCodeInputView(TemplateView):
    """View for manual code input"""

    template_name = 'manual_code_input.html'


class IndexView(TemplateView):
    """View for index page"""

    template_name = 'index.html'


def refactor_code_handler(request: WSGIRequest) -> HttpResponse:
    """Handler for code refactoring"""

    return render(
        request,
        'refactoring_results.html',
        {'results': 'TODO'},
    )


class InstructionView(TemplateView):
    """View for instruction page"""

    template_name = 'instruction.html'


class RulesView(TemplateView):
    """View for rules page"""

    template_name = 'rules.html'


class RefactoringResultsView(TemplateView):
    """View for refactoring results page"""

    template_name = 'refactoring_results.html'
