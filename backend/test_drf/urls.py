from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('products/', include('products.urls')),
    path('model/', include('model_api.urls')),
    # path('api/', include('api.urls'))
]
