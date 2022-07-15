"""Mixins for tests"""

from django.test import TestCase
from django.contrib.auth import get_user_model

from config.constants.tests import (
    ACCOUNT, LOGIN, SUPERUSER_USERNAME, SUPERUSER_PASSWORD,
)


class Test302IfNotAuthorizedMixin(TestCase):
    """Mixin for testing status code is 302 if user is not authorized"""

    def _test_302_if_not_authorized(self, path: str) -> None:
        """Test status code is 302 if user is not authorized"""

        response = self.client.get(path)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            ACCOUNT + LOGIN + '?next=' + path,
        )


class Test200IfAuthorizedMixin(TestCase):
    """Mixin for testing status code is 200 if user authorized"""

    def _test_200_if_authorized(self, path: str) -> None:
        """Test status code is 200 if user is authorized"""

        self.__authorize()

        response = self.client.get(path)

        self.assertEqual(response.status_code, 200)

    def __authorize(self) -> None:
        """Create user and authorize"""

        get_user_model().objects.create_user(
            username=SUPERUSER_USERNAME, password=SUPERUSER_PASSWORD,
        )

        self.client.post(
            ACCOUNT + LOGIN,
            {
                'username': SUPERUSER_USERNAME,
                'password': SUPERUSER_PASSWORD,
            },
        )
