# hip-flask

<p align="center">
    <img src="https://raw.githubusercontent.com/rancorm/hip-flask/main/flask.svg" width="200" height="200" alt="Hip flask" />
</p>

Lightweight Flask extension to simplify the integration of CSS and JavaScript files
into your applications.

## Start here 

Install the extension:

```sh
pip install hip-flask
```

Considering the minimal flask application factory below in `hipapp.py` as an example:

```python
from flask import Flask
from hip_flask import HipExtension

def create_app():
    app = Flask(__name__)

    hip = HipExtension(app)

    # Meta tags
    hip.meta(name="charset", value="utf-8")
    hip.meta(name="description", content="Timeline event tracker")
    hip.meta(name="keywords", content=["HTML", "CSS", "JavaScript"])
    
    # Stylesheets
    hip.static_link("css/hipapp.css")

    # Scripts
    hip.static_script("js/hipapp.js")

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
```

In the template use macros `hip_links`, `hip_scripts`, or `hip_metas` to retrieve link,
script, and meta tags respectively for use in the template:

### Stylesheets

```python
{% block stylesheets %}
{% for css in macros.hip_links() %}{{ css.as_tag() }}{% endfor %}
{% endblock %}
```

### Meta tags

```python
{% block metas %}
{% for meta in macros.hip_metas() %}{{ meta.as_tag() }}{% endfor %}
{% endblock %}
```

## Contributing

You know the drill. Fork and get to work.
