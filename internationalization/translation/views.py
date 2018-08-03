# coding: utf-8


from django.utils import translation
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view

from rest_framework.response import Response


@api_view()
def hello(request):
    print(request.META)
    data = {}
    data['result'] = _('Test')
    return Response(data)
