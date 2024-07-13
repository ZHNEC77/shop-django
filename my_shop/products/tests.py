from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from products.models import Product, ProductCategory
# Create your tests here.


class TestIndexView(TestCase):

    def test_view(self):
        path = reverse("index")
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data["title"], "Shop")
        self.assertTemplateUsed(response, "products/index.html")


class TestMainPageView(TestCase):
    fixtures = ["categories.json", "product.json"]

    def setUp(self):
        self.products = Product.objects.all()

    def test_list(self):
        path = reverse("products:main_page")
        response = self.client.get(path)

        self._common_tests(response)
        self.assertEqual(
            list(
                response.context_data["object_list"]), list(self.products[:12]
                                                            )
        )

    def test_list_with_category(self):
        category = ProductCategory.objects.first()
        path = reverse("products:category", kwargs={
                       "category_id": category.id})
        response = self.client.get(path)

        self._common_tests(response)
        self.assertEqual(
            list(response.context_data["object_list"]),
            list(self.products.filter(category_id=category.id)),
        )

    def _common_tests(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data["title"], "Shop - Каталог")
        self.assertTemplateUsed(response, "products/main_page.html")
