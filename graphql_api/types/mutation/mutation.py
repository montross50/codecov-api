from ariadne import MutationType

from .create_api_token import resolve_create_api_token

mutation_bindable = MutationType()

# Here, bind the resolvers from each subfolder to the Mutation type
mutation_bindable.field("createApiToken")(resolve_create_api_token)
