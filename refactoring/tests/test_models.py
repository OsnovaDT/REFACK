"""Tests for models of refactoring app"""

from django.contrib.auth import get_user_model
from django.db.models import CASCADE
from django.test import TestCase, tag

from refactoring.models import RefactoringRecommendation
from config.tests.utils import run_field_attribute_test


User = get_user_model()


@tag('refactoring_recommendation')
class RefactoringRecommendationTests(TestCase):
    """Tests for RefactoringRecommendation model"""

    __TEST_USERNAME = 'test_username'

    __TEST_PASSWORD = 'test_password'

    def setUp(self) -> None:
        User.objects.create(
            username=self.__TEST_USERNAME, password=self.__TEST_PASSWORD,
        )

        RefactoringRecommendation.objects.create(
            user=User.objects.get(username=self.__TEST_USERNAME),
            code='def a(): return 1',
            recommendation='recommendation',
        )

        self.field_and_verbose_name = {
            'user': 'пользователь',
            'code': 'исходный код',
            'recommendation': 'рекомендация по рефакторингу',
            'date': 'дата рефакторинга',
        }

        self.field_and_max_length = {
            'code': 10_000,
        }

        self.field_and_auto_now_add = {
            'date': True,
        }

    def test_on_delete(self) -> None:
        """Test on_delete attribute for fields"""

        user_field = RefactoringRecommendation._meta.get_field('user')

        self.assertEqual(user_field.remote_field.on_delete, CASCADE)

    def test_verbose_name(self) -> None:
        """Test verbose_name attribute for fields"""

        run_field_attribute_test(
            RefactoringRecommendation, self,
            self.field_and_verbose_name, 'verbose_name',
        )

    def test_max_length(self) -> None:
        """Test max_length attribute for fields"""

        run_field_attribute_test(
            RefactoringRecommendation, self,
            self.field_and_max_length, 'max_length',
        )

    def test_auto_now_add(self) -> None:
        """Test auto_now_add attribute for fields"""

        run_field_attribute_test(
            RefactoringRecommendation, self,
            self.field_and_auto_now_add, 'auto_now_add',
        )

    def test_model_verbose_name(self) -> None:
        """Test RefactoringRecommendation verbose_name"""

        self.assertEqual(
            RefactoringRecommendation._meta.verbose_name,
            'Рекомендация по рефакторингу',
        )

    def test_model_verbose_name_plural(self) -> None:
        """Test RefactoringRecommendation verbose_name_plural"""

        self.assertEqual(
            RefactoringRecommendation._meta.verbose_name_plural,
            'Рекомендации по рефакторингу',
        )

    def test_model_ordering(self) -> None:
        """Test RefactoringRecommendation ordering"""

        self.assertEqual(
            RefactoringRecommendation._meta.ordering,
            ['-date'],
        )
