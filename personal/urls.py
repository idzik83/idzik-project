from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'idzik_test_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.PersonalView.as_view()),
)
