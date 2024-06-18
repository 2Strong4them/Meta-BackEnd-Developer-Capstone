from django.test import TestCase
from django.urls import reverse
from Restaurant.models import Menu
from Restaurant.serializer import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        self.menu1 = Menu.objects.create(title="Menu 1", price=50, inventory=52)
        self.menu2 = Menu.objects.create(title="Menu 2", price=40, inventory=63)

    def test_getall(self):
        # Retrieve all Menu objects added for the test purpose
        response = self.client.get(reverse('MenuItemsViews'))
        
        # Serialize the data
        serialized_data = MenuSerializer([self.menu1, self.menu2], many=True).data

        # Check if the serialized data equals the response
        self.assertEqual(response.data, serialized_data)