# encoding: utf-8
# Author: Cai Chenyi

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.conf import settings

class LoginRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            if request.is_ajax():
                return JsonResponse({'status': 401})
            else:
                return HttpResponseRedirect(settings.LOGIN_URL)
        return super().dispatch(request, *args, **kwargs)
