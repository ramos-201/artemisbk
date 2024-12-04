import graphene
from graphene import Mutation, String


class RegisterUser(Mutation):
    class Arguments:
        name = String(required=True)
        last_name = String(required=True)
        user = String(required=True)
        email = String(required=True)
        mobile_phone = String(required=True)
        password = String(required=True)

    response = String()  # message txt
    data = String()  # object data | name ...

    @classmethod
    async def mutate(cls, root, info, name, last_name, user, email, mobile_phone, password):
        return RegisterUser(
            response='User registered successfully',
            data=name,  # or any other data you want to return
        )


class Mutation(graphene.ObjectType):
    register_user = RegisterUser.Field()
