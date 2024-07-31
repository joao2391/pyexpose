import unittest
from src import expose


class ExposeHtmlDocumentTests(unittest.TestCase):
    
    def test_count_css(self):
        url = "https://www.w3schools.com/jsref/event_onclick.asp"
        obj = expose.ExposeHtmlDocument(url)
        self.assertEqual(obj.count_css(), 5)
    
    def test_count_js(self):
        url = "https://www.w3schools.com/jsref/event_onclick.asp"
        obj = expose.ExposeHtmlDocument(url)
        self.assertEqual(obj.count_js(), 20)
    
    def test_total_html_elements(self):
        url = "https://www.w3schools.com/jsref/event_onclick.asp"
        obj = expose.ExposeHtmlDocument(url)
        self.assertEqual(obj.count_total_elements(), 57)
    
    def test_total_meta_elements(self):
        url = "https://www.w3schools.com/jsref/event_onclick.asp"
        obj = expose.ExposeHtmlDocument(url)
        self.assertEqual(obj.count_meta_element(), 11)

    def test_js_content(self):
        url = "https://www.w3schools.com/jsref/event_onclick.asp"
        obj = expose.ExposeHtmlDocument(url)
        self.assertEqual(len(obj.get_js_content()), 12)

    def test_css_content(self):
        url = "https://www.w3schools.com/jsref/event_onclick.asp"
        obj = expose.ExposeHtmlDocument(url)
        self.assertEqual(len(obj.get_css_content()), 4)

    def test_onclick_events(self):
        url = "https://www.w3schools.com/jsref/event_onclick.asp"
        obj = expose.ExposeHtmlDocument(url)
        self.assertEqual(obj.count_onclick_events(), 26)

    def test_count_form_elements(self):
        url = "https://www.w3schools.com/jsref/event_onclick.asp"
        obj = expose.ExposeHtmlDocument(url)
        self.assertEqual(obj.count_forms_elements(), 1)

    def test_form_info(self):
        url = "https://www.w3schools.com/jsref/event_onclick.asp"
        obj = expose.ExposeHtmlDocument(url)
        self.assertEqual(len(obj.get_form_info()), 1)

    def test_page_size(self):
        url = "https://www.w3schools.com/jsref/event_onclick.asp"
        obj = expose.ExposeHtmlDocument(url)
        self.assertEqual(obj.get_page_size(), 395)

    def test_onclick_values(self):
        url = "https://www.w3schools.com/jsref/event_onclick.asp"
        obj = expose.ExposeHtmlDocument(url)
        self.assertEqual(len(obj.get_onclick_values()), 26)

    def test_has_ajax_calls(self):
        url = "https://www.w3schools.com/jsref/event_onclick.asp"
        obj = expose.ExposeHtmlDocument(url)
        self.assertEqual(obj.has_ajax_call(), False)

    def test_report(self):
        url = "https://www.w3schools.com/jsref/event_onclick.asp"
        obj = expose.ExposeHtmlDocument(url)
        self.assertEqual(len(obj.generate_report()), 7)

        
    
    if __name__ == '__main__':
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
    