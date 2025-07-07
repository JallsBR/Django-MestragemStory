from rest_framework.views import APIView
from rest_framework.exceptions import APIException


class Base(APIView):
    def get_enterprise_user(self, user_id):
        ...

        return 

