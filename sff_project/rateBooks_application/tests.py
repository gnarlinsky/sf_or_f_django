from django.test import TestCase


# TODO: separate out into different test files

##############################################################################
# Integration/Functional/Acceptance tests
##############################################################################
from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

class BookListIntegrationTests(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(BookListIntegrationTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(BookListIntegrationTests, cls).tearDownClass()

    def test_book_listed(self):

        # create a test book 
        Book.objects.create(title='Ender\'s Game', author='Orson Scott Card',
                            votes_f=1, votes_sf=9999)

        # make sure it's listed as <first> <last> on the list
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.assertEqual(
            self.selenium.find_elements_by_css_selector('.book')[0].text,
            'Ender\'s Game by Orson Scott Card'
        )

    def test_add_book_linked(self):

        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.assert_(
            self.selenium.find_element_by_link_text('Add a Book')
        )

    def test_add_book(self):

        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.selenium.find_element_by_link_text('add book').click()

        self.selenium.find_element_by_id('id_title').send_keys('test')
        self.selenium.find_element_by_id('id_author').send_keys('book')
        self.selenium.find_element_by_id('id_votes_f').send_keys('1')
        self.selenium.find_element_by_id('id_votes_sf').send_keys('99')

        self.selenium.find_element_by_id("save_book").click()
        self.assertEqual(
            self.selenium.find_elements_by_css_selector('.book')[-1].text,
            'test book'
        )

##############################################################################
# Model tests
##############################################################################
from rateBooks_application.models import Book

class BookTests(TestCase):
    """ Book model tests. """

    def test_str(self):
        """ Test that str() returns  "<Title> by <Author>" """
        book = Book(title='Ender\'s Game', author='Orson Scott Card')
        self.assertEquals(  str(book),
                            'Ender\'s Game by Orson Scott Card'
                         )
##############################################################################
# Views tests
##############################################################################
# testing views - method 1
from django.test.client import Client
from django.test.client import RequestFactory
from rateBooks_application.views import ListBookView

class BookListViewTests(TestCase):
    """ Book list view tests."""

    def test_books_in_the_context(self):

        client = Client()
        response = client.get('/')

        self.assertEquals(list(response.context['object_list']), [])

        Book.objects.create(title='Ender\'s Game', author='Orson Scott Card',
                            votes_f=1, votes_sf=9999)
        response = client.get('/')
        self.assertEquals(response.context['object_list'].count(), 1)

    def test_books_in_the_context_request_factory(self):

        factory = RequestFactory()
        request = factory.get('/')

        response = ListBookView.as_view()(request)

        self.assertEquals(list(response.context_data['object_list']), [])

        Book.objects.create(title='Ender\'s Game', author='Orson Scott Card',
                            votes_f=1, votes_sf=9999)
        response = ListBookView.as_view()(request)
        self.assertEquals(response.context_data['object_list'].count(), 1)


