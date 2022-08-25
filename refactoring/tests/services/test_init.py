"""Test services.__init__ module"""

from django.contrib.auth import get_user_model
from django.test import TestCase, tag

from refactoring.models import RefactoringRecommendation
from refactoring.services import create_refactoring_recommendation
from refactoring.tests.constants import REFACTORING_RECOMMENDATION_DATA


User = get_user_model()


@tag('refactoring_services', 'refactoring_services_init')
class FunctionsTests(TestCase):
    """Test module functions"""

    @classmethod
    def setUpTestData(cls) -> None:
        cls.test_user_name = 'test'

        User.objects.create(username=cls.test_user_name, password="1234")

    def test_create_refactoring_recommendation(self) -> None:
        """Test create_refactoring_recommendation function"""

        self.assertEqual(RefactoringRecommendation.objects.count(), 0)

        create_refactoring_recommendation(REFACTORING_RECOMMENDATION_DATA)

        self.assertEqual(RefactoringRecommendation.objects.count(), 1)

        recommendation = RefactoringRecommendation.objects.last()

        self.assertEqual(
            recommendation.recommendation,
            REFACTORING_RECOMMENDATION_DATA['recommendation'],
        )

        self.assertEqual(
            recommendation.user,
            User.objects.get(username=self.test_user_name),
        )

        self.assertEqual(
            recommendation.code,
            REFACTORING_RECOMMENDATION_DATA[
                'code'
            ].replace('\n', '<br>').replace(' ', '&nbsp;'),
        )

        # Empty data

        create_refactoring_recommendation({})

        self.assertEqual(RefactoringRecommendation.objects.count(), 1)

        # Invalid data

        create_refactoring_recommendation(100)

        self.assertEqual(RefactoringRecommendation.objects.count(), 1)
