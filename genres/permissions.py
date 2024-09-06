'''from rest_framework import permissions

#CLASS DE PERMISSÕES

class GenrePermissionView(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            return request.user.has_perm('genres.view_genres')
        
        if request.method == 'POST':
            return request.user.has_perm('genres.add_genres')
        
        if request.method in ['PATCH', 'PUT',]:
            return request.user.has_perm('genres.change_genres')

        if request.method == 'DELETE':
            return request.user.has_perm('genres.delete_genres')
        
        return False'''