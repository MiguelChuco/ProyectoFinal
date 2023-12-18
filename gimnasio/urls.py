from django.urls import path
from .views import (
    home, register, login_view, logout_view,
    agregar_actividad, editar_actividad, eliminar_actividad,
    agregar_producto, editar_producto, eliminar_producto, contacto
)

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('agregar_actividad/', agregar_actividad, name='agregar_actividad'),
    path('editar_actividad/<int:actividad_id>/', editar_actividad, name='editar_actividad'),
    path('eliminar_actividad/<int:actividad_id>/', eliminar_actividad, name='eliminar_actividad'),
    path('agregar_producto/', agregar_producto, name='agregar_producto'),
    path('editar_producto/<int:producto_id>/', editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
    path('contacto/', contacto, name='contacto'),
    # Agrega aquí las demás URL específicas de gimnasio
]
