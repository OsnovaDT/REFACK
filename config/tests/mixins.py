"""Mixins for tests"""

from django.contrib.auth import get_user_model
from django.test import TestCase

from config.tests.constants import (
    ACCOUNT, LOGIN, SUPERUSER_USERNAME, SUPERUSER_PASSWORD,
)


class TestURLMixin(TestCase):
    """Mixin for testing status code """

    def _test_url(
            self, path: str, expected_status_code=302,
            is_authorized=False, data=None) -> None:
        """Test status code if user is authorized"""

        if is_authorized:
            self.__authorize()

        if data:
            response = self.client.post(path, data)
        else:
            response = self.client.get(path)

        self.assertEqual(response.status_code, expected_status_code)

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
