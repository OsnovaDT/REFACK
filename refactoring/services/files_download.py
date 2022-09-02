"""Services for downloading files with refactoring recommendations"""

from json import loads

from dicttoxml import dicttoxml
from django.http import FileResponse, JsonResponse


def get_xml_file_content(file_content: str) -> str:
    """Return file content converted for XML"""

    xml_file_content = ""

    if isinstance(file_content, str):
        xml_file_content = str(dicttoxml(loads(file_content)))

    return xml_file_content


def get_response_with_file(
        file_content: str, file_name: str) -> FileResponse | JsonResponse:
    """Return FileResponse or JsonResponse with file"""

    if isinstance(file_content, str) and isinstance(file_name, str):
        _, file_extension = file_name.split(".")

        if file_extension == "json":
            response = _get_json_response(file_content)
        else:
            response = FileResponse(
                file_content,
                content_type=f"application/{file_extension}",
            )

        _add_file_disposition_to_response(response, file_name)
    else:
        response = FileResponse("", content_type="application/json")

    return response


def _add_file_disposition_to_response(
        response: FileResponse | JsonResponse, file_name: str) -> None:
    """Add file Content-Disposition to the response"""

    if not isinstance(file_name, str):
        file_name = ""

    if isinstance(response, (FileResponse, JsonResponse)):
        response["Content-Disposition"] = f"attachment; filename={file_name};"


def _get_json_response(file_content: str) -> JsonResponse:
    """Return JsonResponse with file"""

    if isinstance(file_content, str):
        json_response = JsonResponse(
            loads(file_content),
            json_dumps_params={"ensure_ascii": False},
        )
    else:
        json_response = JsonResponse({})

    return json_response
