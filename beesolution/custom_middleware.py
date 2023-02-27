
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
import json


class NonHtmlDebugToolbarMiddleware(MiddlewareMixin):

    def process_response(self, request, response):

        if (response["Content-Type"] == "application/json") and ("__debug__" not in request.path_info):
            content = json.dumps(json.loads(response.content), sort_keys=True, indent=2, ensure_ascii=False)
            response = HttpResponse(u'<html><body><pre>{}</pre></body></html>'.format(content))
        return response