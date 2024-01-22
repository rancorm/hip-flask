import pytest

from flask import Flask
from hip_flask import HipExtension

@pytest.fixture
def app():
    app = Flask(__name__)
    
    app.config['TESTING'] = True
    hip = HipExtension(app)

    return app

def test_hip_init(app):
    assert 'hip' in app.extensions

def test_hip_meta(app):
    hip = HipExtension(app)

    hip.meta(hip.Meta.CHARSET, "utf-8")
    
    assert not 'charset' in hip.metas

def test_hip_script(app):
    hip = HipExtension(app)

    hip.script("js/main.js")

    assert not 'script' in hip.scripts
