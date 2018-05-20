from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from django.views.static import serve


# from Dashboard.views import GetAjaxViewDash

urlpatterns = [
     url(r'^admin/', include([
            # User URL's
            url(r'^adduser/', views.addUser, name='registration.admin.adduser'),
            url(r'^saveuser', views.saveUser, name='registration.admin.saveuser'),
            url(r'^edituser/(?P<edit_id>.+)', views.editUser, name='registration.admin.edituser'),
            url(r'^updateuser', views.updateUser, name='registration.admin.updateuser'),
     ]
     )),
 ]
if settings.DEBUG:
    # import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



