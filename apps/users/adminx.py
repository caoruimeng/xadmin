import xadmin
from .models import UserProfile
from xadmin import views


class BaseSetting:
    """
    后台修改需要的配置
    """
    # enable_themes = True  # 开启主题功能
    # use_bootswatch = True


class GlobalSettings:
    """
    后台修改
    """
    site_title = '在线学习网'
    site_footer = '在线学习网'
    # menu_style = 'accordion'  # 开启分组折叠

    def get_site_menu(self):
        return [
            {
                'title': '测试的',
                'icon': 'fa fa-bar-chart-o',
                'menus': (
                    {
                        'title': '测试子菜单1',  # 这里是你菜单的名称
                        'url': '/xadmin/test_view',  # 这里填写你将要跳转url
                        'icon': 'fa fa-cny'  # 这里是bootstrap的icon类名，要换icon只要登录bootstrap官网找到icon的对应类名换上即可
                    },
                    {
                        'title': '测试子菜单2',
                        'url': 'http://www.taobao.com',
                        'icon': 'fa fa-cny'
                    }
                )
            }
        ]


class UserProfileAdmin(object):
    list_display = ['username', 'email', 'nick_name', 'gender']


# 注册你上面填写的url

from .views import TestView  # 从你的app的view里引入你将要写的view，你也可以另外写一个py文件，把后台的view集中在一起方便管理



xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
# xadmin.site.register(views.CommAdminView, GlobalSettings)
