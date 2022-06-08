"""Views of refactoring app"""

from logging import getLogger

from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse

from refactoring.code_inspector import CodeInspector


class ManualCodeInputView(TemplateView):
    """View for manual code input"""

    template_name = 'manual_code_input.html'


class IndexView(TemplateView):
    """View for index page"""

    template_name = 'index.html'


def refactor_code_handler(request: WSGIRequest) -> HttpResponse:
    """Handler for code refactoring"""

    try:
        code = request.POST['code']

        code_inspector = CodeInspector(code)
        code_errors = code_inspector.errors

        for key, value in code_errors.items():
            code_errors[key] = ', '.join(value)
        if len(code_errors) == 0:
            code_errors = 'Ваш код чистый!'
    except Exception as error:
        getLogger().error(f'Error: {error}')
        code_errors = {}

    return render(
        request, 'refactoring_results.html', {'results': code_errors},
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
