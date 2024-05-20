
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from .models import Alert
from .serializers import AlertSerializer

from chat.models import Room
from chat.serializers import RoomSerializer

@api_view(['POST'])
def login(request):

    username = request.data.get('username')
    password = request.data.get('password')

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response('User invalid', status=status.HTTP_401_UNAUTHORIZED)

    pwd_valid = check_password(password, user.password)

    if not pwd_valid:
        return Response('Password invalid', status=status.HTTP_401_UNAUTHORIZED)

    token, _= Token.objects.get_or_create(user=user)

    return Response('Token_'+token.key)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def alerts(request):
    print(request.user.id)

    alerts = Alert.objects.filter(user_id=request.user.id)
    selializer = AlertSerializer(alerts, many=True)

    return Response(selializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def rooms(request):
    selializer = RoomSerializer(Room.objects.all(), many=True)
    return Response(selializer.data)


@api_view(['POST'])
def logout(request):
    token = request.data.get('token')

    if len(token.split('_')) == 2:
        token_name, token_key = token.split('_')
        if token_name=='Token':
            try:
                Token.objects.get(key=token_key).delete()
            except Token.DoesNotExist:
                pass
    return Response('ok')
