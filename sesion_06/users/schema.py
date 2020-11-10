"""Movies app GraphQL Schema"""

from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth import authenticate

import graphene
import jwt


class LoginMutation(graphene.Mutation):
    """Gets token"""
    class Arguments:
        """These are the arguments to be passed to mutation"""
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    token = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, username, password):
        """Creates token"""
        user = authenticate(username=username, password=password)

        if not user:
            raise Exception('Invalid credentials')

        encoded = jwt.encode(
            payload={'uid': user.id, 'exp': datetime.utcnow() +
                     timedelta(days=2)},
            key=settings.SECRET_KEY,
            algorithm='HS256'
        )

        token = encoded.decode()

        return LoginMutation(token=token)

# Root mutation


class Mutation(graphene.ObjectType):
    """Mutates GraphQL data"""
    login = LoginMutation.Field()
