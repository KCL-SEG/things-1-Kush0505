from django.core.exceptions import ValidationError
from django.test import TestCase
from things.models import Thing

# Create your tests here.

class BaseModelTest(TestCase):
    def setUp(self):
        self.thing = Thing(name="Foobar", description = "Foobar Thing", quantity = 2)

    def test_valid_thing(self):
        self._assert_thing_is_vaild("Could not create thing with the required attributes")
    
    def _assert_thing_is_valid(self, message="a valid thing was rejected"):
        try:
            self.thing.full_clean()
        except ValidationError:
            self.fail(message)