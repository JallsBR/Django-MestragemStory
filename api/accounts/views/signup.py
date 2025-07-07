from accounts.views.base import Base
from accounts.auth import Authentication
from accounts.serializers import UserSerializer

from rest_framework.response import Response

class Signup(Base):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        user = Authentication.signup(self, username=username, email=email, password=password)

        serializer = UserSerializer(user)

        return Response({"user": serializer.data})