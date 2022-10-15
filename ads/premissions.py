from django.http import Http404
from rest_framework import permissions

from ads.models import Ad
from selections.models import Selection
from users.models import UserRoles


class SelectionChangePermissions(permissions.BasePermission):
    message = 'You can only change your selections'

    def has_permission(self, request, view):
        try:
            entity = Selection.objects.get(pk=view.kwargs['pk'])
        except Selection.DoesNotExist:
            raise Http404

        if entity.owner_id == request.user.id:
            return True
        return False
        

class AdChangePermissions(permissions.BasePermission):
    message = 'You can only change your ads'

    def has_permission(self, request, view):
        if request.user.role in [UserRoles.MODERATOR, UserRoles.ADMIN]:
            return True

        try:
            entity = Ad.objects.get(pk=view.kwargs['pk'])
        except Ad.DoesNotExist:
            raise Http404

        if entity.author_id == request.user.id:
            return True
        return False
