from django.conf.urls import url

from members import views

urlpatterns = [

	# ex: /members/
    url(r'^$', views.index, name='index'),
    # ex: /members/1/
    url(r'^(?P<Dept_Name>[a-z]+)/$', views.detail, name='detail'),

]