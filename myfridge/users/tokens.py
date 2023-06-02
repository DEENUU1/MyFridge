from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


class TokenGenerator(PasswordResetTokenGenerator):
    """
    A custom token generator for generating tokens for activating user accounts.
    """

    def _make_hash_value(self, user, timestamp):
        """
        A method that overrides the built-in _make_hash_value method in the PasswordResetTokenGenerator
        class to generate a hash value based on the user's primary key, the timestamp, and whether the user is active.
        """
        return (
            six.text_type(user.pk)
            + six.text_type(timestamp)
            + six.text_type(user.is_active)
        )


account_activation_token = TokenGenerator()
