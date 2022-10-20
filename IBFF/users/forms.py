from django_registration.forms import RegistrationForm
from users.models import IBFFUser


class IBFFUserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = IBFFUser
