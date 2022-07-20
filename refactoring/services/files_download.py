"""Services for files download"""

from json import loads

from dicttoxml import dicttoxml
from django.http import FileResponse, JsonResponse


def get_xml_file_content(file_content: str) -> str:
    """Return file content converted for XML"""

    return str(dicttoxml(loads(file_content)))


def get_response_with_file(
        file_content: str, file_name: str,
        extension: str) -> FileResponse | JsonResponse:
    """Return FileResponse or JsonResponse with file"""

    if extension == 'json':
        response = _get_json_file_response(file_content)
    else:
        response = FileResponse(
            file_content, content_type=f'application/{extension}',
        )

    _add_file_disposition_to_response(response, f'{file_name}.{extension}')

    return response


def _add_file_disposition_to_response(
        response: FileResponse | JsonResponse, file_name: str) -> None:
    """Add file Content-Disposition to the response"""

    response['Content-Disposition'] = f'attachment; filename={file_name};'


def _get_json_file_response(file_content: str) -> JsonResponse:
    """Return JsonResponse with file"""

    return JsonResponse(
        loads(file_content), json_dumps_params={'ensure_ascii': False},
    )
