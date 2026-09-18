from django.test import TestCase
from .models import FoodModel


class FoodModelTest(TestCase):

    def test_food_name(self):
        food = FoodModel.objects.create(
            name="Chicken Biryani",
            price=200,
            description="This is the best biryani in the world"
        )

        self.assertEqual(food.name, "Chicken Biryani")