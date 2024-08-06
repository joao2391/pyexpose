import unittest
from src.py_expose_html import expose
from unittest.mock import patch, MagicMock
from pathlib import Path


class ExposeHtmlDocumentTests(unittest.TestCase):

    def setUp(self):
        self.url = "https://www.w3schools.com/jsref/event_onclick.asp"
        relative_path = 'mock_data.html'
        dir = Path(__file__).parent
        absolute_path = dir.joinpath(relative_path)
        with open(absolute_path, "r") as file:
            self.html = file.read()
    
    @patch("urllib.request.urlopen")
    def test_count_css(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status = 200

        mock_response.read.return_value = self.html

        mock_requests.return_value = mock_response

        obj = expose.ExposeHtmlDocument(self.url)
        self.assertEqual(obj.count_css(), 1)
    
    @patch("urllib.request.urlopen")
    def test_count_js(self, mock_requests):
        # url = "https://www.w3schools.com/jsref/event_onclick.asp"
        # obj = expose.ExposeHtmlDocument(url)
        mock_response = MagicMock()
        mock_response.status = 200

        mock_response.read.return_value = self.html

        mock_requests.return_value = mock_response

        obj = expose.ExposeHtmlDocument(self.url)
        self.assertEqual(obj.count_js(), 3)
    
    @patch("urllib.request.urlopen")
    def test_total_html_elements(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status = 200

        mock_response.read.return_value = self.html

        mock_requests.return_value = mock_response

        obj = expose.ExposeHtmlDocument(self.url)
        self.assertEqual(obj.count_total_elements(), 11)
    
    @patch("urllib.request.urlopen")
    def test_total_meta_elements(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status = 200

        mock_response.read.return_value = self.html

        mock_requests.return_value = mock_response

        obj = expose.ExposeHtmlDocument(self.url)
        self.assertEqual(obj.count_meta_elements(), 2)

    
    @patch("urllib.request.urlopen")
    def test_js_content(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status = 200

        mock_response.read.return_value = self.html

        mock_requests.return_value = mock_response

        obj = expose.ExposeHtmlDocument(self.url)
        self.assertEqual(len(obj.get_js_content()), 1)

    
    @patch("urllib.request.urlopen")
    def test_css_content(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status = 200

        mock_response.read.return_value = self.html

        mock_requests.return_value = mock_response

        obj = expose.ExposeHtmlDocument(self.url)
        self.assertEqual(len(obj.get_css_content()), 1)

    
    @patch("urllib.request.urlopen")
    def test_onclick_events(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status = 200

        mock_response.read.return_value = self.html

        mock_requests.return_value = mock_response

        obj = expose.ExposeHtmlDocument(self.url)
        
        self.assertEqual(obj.count_onclick_events(), 1)

    
    @patch("urllib.request.urlopen")
    def test_count_form_elements(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status = 200

        mock_response.read.return_value = self.html

        mock_requests.return_value = mock_response

        obj = expose.ExposeHtmlDocument(self.url)

        self.assertEqual(obj.count_forms_elements(), 1)

    
    @patch("urllib.request.urlopen")
    def test_form_info(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status = 200

        mock_response.read.return_value = self.html

        mock_requests.return_value = mock_response

        obj = expose.ExposeHtmlDocument(self.url)

        self.assertEqual(len(obj.get_form_info()), 1)

    
    @patch("urllib.request.urlopen")
    def test_page_size(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status = 200

        mock_response.read.return_value = self.html

        mock_requests.return_value = mock_response

        obj = expose.ExposeHtmlDocument(self.url)

        self.assertEqual(obj.get_page_size(), 0)

    
    @patch("urllib.request.urlopen")
    def test_onclick_values(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status = 200

        mock_response.read.return_value = self.html

        mock_requests.return_value = mock_response

        obj = expose.ExposeHtmlDocument(self.url)

        self.assertEqual(len(obj.get_onclick_values()), 1)

    
    @patch("urllib.request.urlopen")
    def test_has_ajax_calls(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status = 200

        mock_response.read.return_value = self.html

        mock_requests.return_value = mock_response

        obj = expose.ExposeHtmlDocument(self.url)

        self.assertEqual(obj.has_ajax_call(), True)

    
    @patch("urllib.request.urlopen")
    def test_report(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status = 200

        mock_response.read.return_value = self.html

        mock_requests.return_value = mock_response

        obj = expose.ExposeHtmlDocument(self.url)

        self.assertEqual(len(obj.generate_report()), 7)

        
    
    if __name__ == '__main__':
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
    