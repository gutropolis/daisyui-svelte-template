import graphene

from apps.plan.schema import PlanMutation, PlanQuery
from apps.subscription.schema import SubscriptionMutation, SubscriptionQuery
from graphql_auth import mutations as auth_mutations
from graphql_auth.schema import MeQuery, UserQuery


class AuthMutation(graphene.ObjectType):
	register = auth_mutations.Register.Field()
	verify_account = auth_mutations.VerifyAccount.Field()
	resend_activation_email = auth_mutations.ResendActivationEmail.Field()
	send_password_reset_email = auth_mutations.SendPasswordResetEmail.Field()
	password_reset = auth_mutations.PasswordReset.Field()
	password_change = auth_mutations.PasswordChange.Field()
	update_account = auth_mutations.UpdateAccount.Field()
	token_auth = auth_mutations.ObtainJSONWebToken.Field()
	refresh_token = auth_mutations.RefreshToken.Field()
	revoke_token = auth_mutations.RevokeToken.Field()


class Query(MeQuery, UserQuery, PlanQuery, SubscriptionQuery, graphene.ObjectType):
	"""Root GraphQL query composed from every app-level query plus auth helpers."""


class Mutation(AuthMutation, PlanMutation, SubscriptionMutation, graphene.ObjectType):
	"""Root GraphQL mutation composed from every app-level mutation plus auth flows."""


schema = graphene.Schema(query=Query, mutation=Mutation)
