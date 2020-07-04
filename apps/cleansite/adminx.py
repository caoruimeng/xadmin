import xadmin
from xadmin import views
import json
from .models import CleanSite
from .views import TestView
from xadmin.views.base import CommAdminView, filter_hook


class CleanSiteAdmin(object):
    list_display = ['name', 'phone', 'desc']
    object_list_template = 'test.html'

    # 重写方法，把要展示的数据更新到 context
    @filter_hook
    def get_context(self):
        # context = TestView.get_context(self)
        context = super().get_context()
        # context = super(TestView, self).get_context()
        address_point = CleanSite.objects.all()

        address_longitude = []
        address_latitude = []
        address_data = []
        for i in range(len(address_point)):
            address_longitude.append(float(address_point[i].longitude))
            address_latitude.append(float(address_point[i].dimension))
            address_data.append(address_point[i].name)

        context.update(
            {
                'address_longitude': json.dumps(address_longitude),
                'address_latitude': json.dumps(address_latitude),
                'address_data': json.dumps(address_data)
            }
        )

        return context


xadmin.site.register(CleanSite, CleanSiteAdmin)
