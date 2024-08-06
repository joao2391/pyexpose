from bs4 import BeautifulSoup
import urllib.request


class ExposeHtmlDocument:


    def __init__(self, url):

        if not url:
            raise ValueError("URL or PATH is required")

        self.url = url
        #self.path = path
        global html, head, body, response

        if self.url != '':

            response = urllib.request.urlopen(self.url)

            if response.status != 200:
                raise ConnectionError(f"HTTP Status Code is not 200 -> {self.url}")

            html = response.read()

        # else:
        #     file = open(path, 'r')
        #     html = file
        
        soup = BeautifulSoup(html, features="html.parser")

        head = soup.find("head")

        body = soup.find("body")

        #file.close()


    def count_css(self) -> int:
        """
        Return total of CSS files referenced in the html page
        """
        count_css = 0

        if head:
            links = head.find_all("link")

            if links:
                for rel in links:
                    if "stylesheet" in rel.get("rel"):
                        count_css += 1

        if body:
            links = body.find_all("link")

            if links:
                for rel in links:
                    if "stylesheet" in rel.get("rel"):
                        count_css += 1

        return count_css

    def count_js(self) -> int:
        """
        Return total of JS files referenced in the html page
        """
        count_js = 0

        if head:
            scripts = head.find_all("script")

            if scripts:
                count_js += len(scripts)

        if body:
            scripts = body.find_all("script")

            if scripts:
                count_js += len(scripts)

        return count_js

    def count_total_elements(self) -> int:
        """
        Return the total of Html Elements
        """
        count_html = 0

        if head:
            for x in head:
                if x != '\n':
                    count_html += 1

        if body:
            for x in body:
                if x != '\n':
                    count_html += 1

        return count_html

    def count_meta_elements(self) -> int:
        """
        Return the total of META elements
        """

        count_meta = 0

        if head:
            metas = head.find_all("meta")

        count_meta += len(metas)

        return count_meta

    def get_js_content(self) -> list:
        """
        Returns a list of JavaScript code
        """
        lst_js = []

        if head:
            js = head.find_all("script")
            for x in js:
                lst_js.append(x.string)

        if body:
            js = body.find_all("script")
            for x in js:
                lst_js.append(x.string)

        lst_js = list(filter(None, lst_js))

        return lst_js

    def get_css_content(self) -> list:
        """
        Returns a list of CSS code
        """
        lst_css = []

        if head:
            css = head.find_all("style")
            for x in css:
                lst_css.append(x.string)

        if body:
            js = body.find_all("style")
            for x in js:
                lst_css.append(x.string)

        lst_css = list(filter(None, lst_css))

        return lst_css

    def count_onclick_events(self) -> int:
        """
        Returns the total of onclick events in all elements in the html
        """
        count_onclick = 0

        if body:
            attrs = []
            for elm in body.find_all():
                attrs.append(elm.attrs)

        attrs = list(filter(None, attrs))

        for x in attrs:
            if "onclick" in x.keys():
                count_onclick += 1

        return count_onclick

    def count_forms_elements(self) -> int:
        """
        Returns the total of Forms elements in html page
        """
        count_forms = 0

        if body:
            elem = body.find_all("form")
            count_forms = len(elem)

        return count_forms

    def get_form_info(self) -> dict:
        """
        Returns Action and HttpMethod from all Form elements
        """
        form_info = {}

        if body:
            form_elem = body.find_all("form")

            for x in form_elem:
                action = x.attrs.get("action")
                method = x.attrs.get("method")

                form_info[action] = method

        return form_info

    def get_page_size(self) -> int:
        """
        Returns the page size in Kb
        """
        page_size = 0
        size = int(response.headers["Content-Length"]) / 1024
        page_size = round(size)

        return page_size

    def get_onclick_values(self) -> list:
        """
        Returns a list containing onclick events value
        """
        onclick_values = []

        if body:
            attrs = []
            for elm in body.find_all():
                attrs.append(elm.attrs)

        attrs = list(filter(None, attrs))

        for x in attrs:

            if "onclick" in x.keys():
                onclick_values.append(x["onclick"])

        return onclick_values

    def has_ajax_call(self) -> bool:
        """
        Check if there are Ajax calls in any script tag
        """
        has_call = False
        lst_js = []

        if body:
            js = body.find_all("script")
            for x in js:
                lst_js.append(x.string)

            lst_js = list(filter(None, lst_js))

            for x in lst_js:
                if 'ajax' in x:
                    has_call = True

        return has_call

    def generate_report(self) -> dict:
        """
        Returns a dictionary summarizing all results
        """
        report = {}

        report['total_css'] = self.count_css()
        report['total_js'] = self.count_js()
        report['total_elements'] = self.count_total_elements()
        report['total_meta_elements'] = self.count_meta_elements()
        report['total_onclick_events'] = self.count_onclick_events()
        report['total_form_elements'] = self.count_forms_elements()
        report['has_ajax_call'] = self.has_ajax_call()

        return report
