"""Mixins for project tests"""

from django.contrib.auth import get_user_model
from django.test import TestCase

from config.tests.constants import (
    ACCOUNT,
    LOGIN,
    SUPERUSER_USERNAME,
    SUPERUSER_PASSWORD,
)


User = get_user_model()


class TestURLMixin(TestCase):
    """Mixin for testing status code"""

    def _test_url(
            self,
            path: str,
            expected_status_code=302,
            is_authorized=False,
            post_data=None) -> None:
        """Test status code if user is authorized"""

        if is_authorized:
            self.__authorize()

        if post_data:
            response = self.client.post(path, post_data)
        else:
            response = self.client.get(path)

        self.assertEqual(response.status_code, expected_status_code)

    def __authorize(self) -> None:
        """Create superuser and authorize"""

        User.objects.create_superuser(
            username=SUPERUSER_USERNAME,
            password=SUPERUSER_PASSWORD,
        )

        self.client.post(
            ACCOUNT + LOGIN,
            {
                "username": SUPERUSER_USERNAME,
                "password": SUPERUSER_PASSWORD,
            },
        )
