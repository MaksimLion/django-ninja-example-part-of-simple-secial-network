from ninja.security import HttpBearer, APIKeyHeader
from rest_framework.authtoken.models import Token


class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
            t = Token.objects.get(key=token)
            return t.user
        except Token.DoesNotExist:
            pass


auth = GlobalAuth()