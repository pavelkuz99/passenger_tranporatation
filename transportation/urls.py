from django.conf.urls import url
from transportation import views


urlpatterns = [
    url(r'^routes/$',
        views.RouteList.as_view(),
        name=views.RouteList.name),
    url(r'^routes/(?P<pk>[0-9]+)/$',
        views.RouteDetail.as_view(),
        name=views.RouteDetail.name),
    url(r'^rides/$',
        views.RideList.as_view(),
        name=views.RideList.name),
    url(r'^rides/(?P<pk>[0-9]+)/$',
        views.RideDetail.as_view(),
        name=views.RideDetail.name),
    # url(r'^players/$',
    #     views.PlayerList.as_view(),
    #     name=views.PlayerList.name),
    # url(r'^players/(?P<pk>[0-9]+)/$',
    #     views.PlayerDetail.as_view(),
    #     name=views.PlayerDetail.name),
    # url(r'^player-scores/$',
    #     views.PlayerScoreList.as_view(),
    #     name=views.PlayerScoreList.name),
    # url(r'^player-scores/(?P<pk>[0-9]+)/$',
    #     views.PlayerScoreDetail.as_view(),
    #     name=views.PlayerScoreDetail.name),
    # url(r'^$',
    #     views.ApiRoot.as_view(),
    #     name=views.ApiRoot.name),
    # url(r'^users/$',
    #     views.UserList.as_view(),
    #     name=views.UserList.name),
    # url(r'^users/(?P<pk>[0-9]+)/$',
    #     views.UserDetail.as_view(),
    #     name=views.UserDetail.name),

]
