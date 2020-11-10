"""Project GraphQL Schema"""

import graphene

from movies.schema import Query as MovieQuery, Mutation as MovieMutation
from users.schema import Mutation as UsersMutation


class Query(MovieQuery):
    """Project root query"""


class Mutation(MovieMutation, UsersMutation):
    """Project root mutation"""


schema = graphene.Schema(query=Query, mutation=Mutation)
