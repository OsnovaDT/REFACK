"""Utils for testing"""

from django.core.exceptions import ObjectDoesNotExist


def run_field_attribute_test(
        model, self_, field_and_attribute_value: dict, attribute_name: str
        ) -> None:
    """Test attribute for all model objects"""

    if not model.objects.exists():
        raise ObjectDoesNotExist(
            f"There is no test objects for {model.__name__} model"
        )

    for object_ in model.objects.all():
        for field, expected_value in field_and_attribute_value.items():
            with self_.subTest(f"{field=}"):
                real_value = getattr(
                    object_._meta.get_field(field),
                    attribute_name,
                )

                self_.assertEqual(real_value, expected_value)
