from .forms import SignupForm
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes


@api_view(['GET'])
def me(request):
    return JsonResponse({
        'id': request.user.id,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
        'uni_id': request.user.uni_id,
        'major': request.user.major,
        'year': request.user.year,
    })
    

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'success'

    form = SignupForm({
        'email': data.get('email'),
        'first_name': data.get('first_name'),
        'last_name': data.get('last_name'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
        'uni_id': data.get('uni_id'),
        'major': data.get('major'),
        'year': data.get('year'),
    })

    if form.is_valid():
        form.save()
    else:
        message = form.errors.as_json()
    
    return JsonResponse({'message': message})