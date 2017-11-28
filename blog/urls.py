



















from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from blog import views

urlpatterns = [
    url(r'^like$', login_required(views.likes_view), name='like'),
    url(r'^posts/(?P<pk>\d+)/details$', login_required(views.PostDetailsView.as_view()), name='post_details'),
    url(r'^posts/(?P<pk>\d+)/comments$',login_required(views.PostCommentsView.as_view()), name='post_comments'),
    url(r'^$', login_required(views.PostListView.as_view()), name='postlist'),

]
