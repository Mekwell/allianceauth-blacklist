from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions

class CustomTokenAuthentication(TokenAuthentication):
    def get_authorization_header(self, request):
        """
        Return request's 'X-API-Token:' header, as a bytestring.
        """
        auth = request.META.get('HTTP_X_API_TOKEN')

        if not auth:
            return None

        return auth.encode()

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token.')

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted.')

        return (token.user, token)
