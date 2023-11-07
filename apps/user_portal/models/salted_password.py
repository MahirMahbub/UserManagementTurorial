import bcrypt
from argon2 import PasswordHasher
from django.db import models
from hashid_field import HashidField


class SaltedPasswordModel(models.Model):
    """
    This model is used to store a salted password.
    """
    # salt = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    hashed_special_key = models.CharField(max_length=255, unique=True)
    is_enabled = models.BooleanField(default=True)

    def check_password(self, password):
        """
        Returns True if the given password is correct, False otherwise.
        """
        raise NotImplementedError("SaltedPasswordModel.check_password() "
                                  "must be implemented in a subclass")

    def set_password(self, password):
        """
        Sets the user's password to the given raw string, taking care of the
        password hashing. Doesn't save the User object.
        """
        salt = bcrypt.gensalt()
        # ph = PasswordHasher()
        # hashed_password = ph.hash(password=password, salt=salt)
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        # self.salt = salt
        self.password = hashed_password

    # class Meta:
    #     abstract = True