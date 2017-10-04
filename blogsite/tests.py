# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class TestHomePage(TestCase):

    def test_uses_index_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, "index.html")

    def test_uses_base_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, "base.html")


class TestNewVisitorHomePage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def test_home_title(self):
        self.browser.get(self.get_full_url('home'))
        self.assertIn("idiot genius", self.browser.title)

    def test_brand_title(self):
        self.browser.get(self.get_full_url('home'))
        brand_title = self.browser.find_element_by_class_name('brand-title')
        self.assertIn("yujinyuz", brand_title.text)