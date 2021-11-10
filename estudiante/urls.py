from django.urls import path,include
from .views import EstudianteView,EstudianteNew,EstudianteEdit,EstuanteDelete

urlpatterns = [
    path("estudiante/",EstudianteView.as_view(),name="estudiante-inicio"),
    path("estudiante/create",EstudianteNew.as_view(),name="estudiante-nuevo"),
    path("estudiante/<pk>/edit",EstudianteEdit.as_view(),name="estudiante-editar"),
    path("estudiante/<pk>/delete",EstuanteDelete.as_view(),name="estudiante-eliminar"),
]
