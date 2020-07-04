from django.shortcuts import render

# Create your views here.
from xadmin.views import CommAdminView, filter_hook


class TestView(CommAdminView):

    @filter_hook
    def get(self, request):
        context = super().get_context()
        title = "会员延期"
        # context["breadcrumbs"].append({'url': '/cwyadmin/', 'title': title})
        context["title"] = title

        return context
