def user_role(request):
    role = None
    if request.user.is_authenticated:
        if request.user.groups.filter(name='Admin').exists():
            role = 'Admin'
        elif request.user.groups.filter(name='Staff').exists():
            role = 'Staff'
        elif request.user.groups.filter(name='Viewer').exists():
            role = 'Viewer'
    return {'user_role': role}