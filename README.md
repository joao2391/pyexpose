# PyExpose ![PyPI](https://img.shields.io/pypi/dd/PyExposeHtml)

PyExpose is a Python library for helping you to scrap web pages. It shows you a lot of information about the page.

## Notes
Version 0.0.1:

- First version

## Installation

Use the package manager to install.

```bash
pip install -U pyexpose
```

## Usage

After install the package:
```python
from py_expose import expose
```

Create an instance of ExposeHtmlDocument. The constructor needs an URL. This URL will be scraped.

```python
expose_doc = new ExposeHtmlDocument('https://some-random-url')
```
 
Return total of CSS files referenced in the html page
```python
total_css = expose_doc.count_css()
```
Return total of JS files referenced in the html page
```python
total_js = expose_doc.count_js()
```
Return total of Html Elements
```python
total_html_elements = expose_doc.count_total_elements()
```
Return total of META elements
```python
total_meta = expose_doc.count_meta_elements()
```
Return all the JS content
```python
total_js_content = expose_doc.get_js_content()
```
Return all the CSS content
```python
total_css_content = expose_doc.get_css_content()
```
Return the total of onclick events in all elements in the html
```python
total_onclick_events = expose_doc.count_onclick_events()
```
Return the total of Forms in html page
```python
total_forms = expose_doc.count_forms_elements()
```
Return the Action and HttpMethod from Form
```python
form_info = expose_doc.get_form_info()
```
Return the size in Kb of the page
```python
page_size = expose_doc.get_page_size()
```
Return the onclick values
```python
onclick_values = expose_doc.get_onclick_values()
```
Return True/False 
```python
has_ajax_call = expose_doc.has_ajax_call()
```
Return the JSON with the amount of info found
```python
report_json = expose_doc.generate_report()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)