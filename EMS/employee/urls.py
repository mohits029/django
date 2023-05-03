from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home),
    path('add-emp/',views.addemployee),
    path('employee/',views.viewemployee),
    path('del-emp/<int:emp_id>', views.deleteemployee),
    path('update-emp/<int:emp_id>', views.updateemployee),
    path('do-update-emp/<int:emp_id>', views.doUpdate),
]
