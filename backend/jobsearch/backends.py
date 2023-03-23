from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User


class SAMLAuthenticationBackend(BaseBackend):
    def authenticate(self, request, remote_user, attributes):
        username = attributes.get('uid', [None])[0]
        email = attributes.get('email', [None])[0]
        first_name = attributes.get('first_name', [None])[0]
        last_name = attributes.get('last_name', [None])[0]

        if not username:
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            if email:
                user = User.objects.create_user(username=username, email=email)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
            else:
                return None

        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
