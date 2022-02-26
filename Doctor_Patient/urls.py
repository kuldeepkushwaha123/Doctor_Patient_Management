from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from account.views import doctor, patient, register,login_user,logout_user,index,deleteUser,update_user

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',index , name="home" ),
    path('login/',login_user,name='login' ),
    path('logout/',logout_user,name='logout' ),
    path('signup/',register,name='signup' ),
    path('delete/<int:pk>/', deleteUser,name="delete"),
    path('update-user/', update_user,name="update-user"),
    path('doctor/', doctor,name="doctor"),
    path('patient/', patient,name="patient"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

