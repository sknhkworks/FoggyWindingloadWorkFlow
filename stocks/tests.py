from django.http import HttpRequest
from django.urls import resolve
from django.contrib.auth import get_user_model
from django.test import TestCase, Client, RequestFactory

from stocks.models import Stocks
from stocks.views import top, stocks_new, stocks_edit, stocks_detail
UserModel = get_user_model()

class TopPageRenderStockTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username="test_user",
            email="test@example.com",
            password="top_secret_pass0001",
        )
        self.stock = Stocks.objects.create(
            title="title1",
            code="print('hello')",
            description="description1",
            created_by=self.user,
        )
    def test_should_return_stocks_title(self):
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.stock.title)

    def test_should_return_username(self):
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.user.username)

#class TopPageViewTest(TestCase):
#    def test_top_returns_200(self):
##        request = HttpRequest()
##        response = top(request)
#        response = self.client.get("/")
#        self.assertEqual(response.status_code, 200)
#
#    def test_top_returns_expected_content(self):
##        request = HttpRequest()
##        response = top(request)
#        response = self.client.get("/")
#        self.assertEqual(response.content, b"Hello World")
class TopPageTest(TestCase):
    def test_top_page_returns_200_and_expected_title(self):
        response = self.client.get("/")
        self.assertContains(response, "Stock", status_code=200)
    def test_top_page_uses_expected_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "stocks/top.html")


class CreateStocksTest(TestCase):
    def test_should_resolve_stocks_new(self):
        found = resolve("/stocks/new/")
        self.assertEquals(stocks_new, found.func)


class StocksDetailTest(TestCase):
    def test_should_resolve_stocks_detail(self):
        found = resolve("/stocks/1/")
        self.assertEquals(stocks_detail, found.func)

class EditStocksTest(TestCase):
    def test_should_resolve_stocks_edit(self):
        found = resolve("/stocks/1/edit/")
        self.assertEquals(stocks_edit, found.func)



