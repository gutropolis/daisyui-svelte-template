import graphene
from graphql_auth import mutations as auth_mutations
from .types import UserType


class UserMutation(graphene.ObjectType):
    # Authentication mutations
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

    # Additional user mutations can be added here
    # For example, update profile, change password, etc.