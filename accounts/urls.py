from django.urls import include, path

from accounts.views import FacebookLogin, GithubLogin

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('github/', GithubLogin.as_view(), name='github_login')
]
