import os
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphql_playground.views import GraphQLPlaygroundView
from graphene_django.views import GraphQLView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=os.environ.get('GRAPHIQL', False)))),
    path('playground/', GraphQLPlaygroundView.as_view(endpoint="http://localhost:8000/graphql/")),
]
