from graphene import Schema
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

from src.api.mutations import Mutation
from src.api.queries import Query

schema = Schema(query=Query, mutation=Mutation)


async def graphql_endpoint(request):
    if request.method == 'POST':
        body = await request.json()
        query = body['query']
        variables = body['variables']

        response = await schema.execute_async(query, variable_values=variables)

        response_data = {
            'data': response.data,
            'errors': [str(error) for error in response.errors] if response.errors else None,
        }

        return JSONResponse(response_data)

    return JSONResponse({'error': ''}, status_code=400)

app = Starlette(
    routes=[
        Route('/graphql', graphql_endpoint, methods=['POST']),
    ]
)
