from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    use_in_migrations = True

    def create_user(self,mobile_number,password=None,**extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if mobile_number:
            user=self.model(mobile_number=mobile_number,**extra_fields)
            user.set_password(password)
            user.save(using=self._db)
        else:
            raise ValueError('Mobile number required')
    def create_superuser(self,mobile_number,password,**extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super user must have is_staff true')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser true.')
        return self.create_user(mobile_number, password, **extra_fields)
