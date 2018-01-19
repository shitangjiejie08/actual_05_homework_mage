from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.conf import settings


class LoginRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            if request.is_ajax():
                return JsonResponse({'status': 401})
            else:
                return HttpResponseRedirect(settings.LOGIN_URL)

        return super().dispatch(request, *args, **kwargs)