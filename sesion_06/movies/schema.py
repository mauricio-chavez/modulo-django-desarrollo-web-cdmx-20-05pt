"""Movies app GraphQL Schema"""

from django.conf import settings

import graphene
from graphene_django import DjangoObjectType
import jwt

from .models import Movie, Director

# Types

class DirectorType(DjangoObjectType):
    """Movie object type for GraphQL"""
    class Meta:
        model = Director
        fields = ["id", "first_name", "last_name", "birthday"]


class MovieType(DjangoObjectType):
    """Movie object type for GraphQL"""
    class Meta:
        model = Movie
        fields = ["id", "name", "release_date", "director"]


# Root query

class Query(graphene.ObjectType):
    """Movie app query root object"""
    get_movies = graphene.List(MovieType)
    get_movie = graphene.Field(MovieType, id=graphene.Int())
    get_directors = graphene.List(DirectorType)
    get_director = graphene.Field(DirectorType, id=graphene.Int())

    def resolve_get_movies(root, info):
        """Get all movies"""
        auth_header = info.context.META.get('HTTP_AUTHORIZATION')
        token = auth_header[7:] if auth_header else ''
        try:
            decoded = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            print('user id:', decoded['uid'])
        except jwt.PyJWTError:
            raise Exception("Invalid token")

        return Movie.objects.prefetch_related('director').all()

    def resolve_get_movie(root, info, id):
        """Get selected movie"""
        return Movie.objects.get(id=id)

    def resolve_get_directors(root, info):
        """Get all directors"""
        return Director.objects.all()

    def resolve_get_director(root, info, id):
        """Get selected director"""
        return Director.objects.get(id=id)


# Mutations

class DirectorMutation(graphene.Mutation):
    """Creates a director"""
    class Arguments:
        """These are the arguments to be passed to mutation"""
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        birthday = graphene.Date(required=True)

    director = graphene.Field(DirectorType)

    @classmethod
    def mutate(cls, root, info, first_name, last_name, birthday):
        """Creates a new director"""
        director = Director.objects.create(
            first_name=first_name,
            last_name=last_name,
            birthday=birthday
        )
        return DirectorMutation(director=director)


class MovieMutation(graphene.Mutation):
    """Creates a movie"""
    class Arguments:
        """These are the arguments to be passed to mutation"""
        name = graphene.String(required=True)
        release_date = graphene.Date(required=True)
        director_id = graphene.Int(required=True)

    movie = graphene.Field(MovieType)

    @classmethod
    def mutate(cls, root, info, name, release_date, director_id):
        """Creates a new movie"""
        movie = Movie.objects.create(
            name=name,
            release_date=release_date,
            director_id=director_id
        )
        return MovieMutation(movie=movie)

# Root mutation


class Mutation(graphene.ObjectType):
    """Mutates GraphQL data"""
    create_director = DirectorMutation.Field()
    create_movie = MovieMutation.Field()
