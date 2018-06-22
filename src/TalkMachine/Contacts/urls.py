from django.urls import path

from .api.viewsets import ContactViewSet


contact_add = ContactViewSet.as_view({'post': 'create'})
contact_exclude = ContactViewSet.as_view({'post': 'destroy'})
contacts_list = ContactViewSet.as_view({'get': 'list'})

urlpatterns = [
    path('<username>/add', contact_add, name='contact-add'),
    path('<username>/exclude', contact_exclude, name='contact-exclude'),
    path('page/<page>', contacts_list, name='contacts-list')
]