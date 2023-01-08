from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        if not email:
            raise ValueError('User must have an email address')
        
        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            first_name = first_name,
            last_name =  last_name,
            email = email,
        )

        user.set_password(password)
        user.save(using = self._db)

        return user
