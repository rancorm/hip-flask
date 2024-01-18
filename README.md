# hip-flask

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

    hip.link_static("css/hipapp.css")

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
```

## Contributing

You know the drill. Fork and get to work.

## Thanks
