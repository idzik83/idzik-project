from django.conf.urls import patterns, include, url
import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'idzik_test_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^login/$', views.login, name='login'),
    url(r'^login/$', views.LoginView.as_view()),
    #url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^logout/$', views.LoginView.logout),
    url(r'^registration/$', views.RegistrationView.as_view()),
    # url(r'^personal/(?P<id>\d+)/$', views.testfunc, name='testfunc'),
    # url(r'^personal/(?P<id>\d+)/$', views.UserCabinet.as_view()),
    url(r'^personal/(?P<id>\d+)/$', login_required(views.UserCabinet.as_view())),
)
