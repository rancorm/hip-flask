from flask import url_for, current_app

class HipExtension:
    """
    Hip Flask extension to simplify CSS and JavaScript integrations
    """

    REL_STYLESHEET = "stylesheet"
    REL_ALTSHEET = "alternate stylesheet"

    class Script:
        def __init__(self, src):
            self.src = src 

        def __str__(self):
            return self.src

        def __repr__(self):
            return self.src

        def as_tag(self):
            return f"<script src=\"{self.src}\"></script>"

    class Link:
        def __init__(self, href, rel, static=False):
            self.href = href
            self.rel = rel
            self.static = static

        def __str__(self):
            return self.href

        def __repr__(self):
            return self.href

        def as_tag(self):
            tag_url = self.href

            if self.static:
                tag_url = url_for('static', filename=self.href)

            return f"<link rel=\"{self.rel}\" href=\"{tag_url}\" />"

    def __init__(self, app=None):
        self.links = []
        self.scripts = []
        self.metas = []

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not hasattr(app, 'extensions'):
            app.extensions = {}

        # Attach to application
        app.extensions['hip'] = self
        app.hip = self

        # Register the macros with the Jinja environment
        if 'macros' not in app.jinja_env.globals:
            app.jinja_env.globals['macros'] = {}

        app.jinja_env.globals['macros']['scripts'] = self._get_scripts
        app.jinja_env.globals['macros']['links'] = self._get_links
        app.jinja_env.globals['macros']['metas'] = self._get_metas

    def script(self, src):
        new_script = self.Script(src)

        self.scripts.append(new_script)

    def link(self, href, rel=REL_STYLESHEET):
        new_link = self.Link(href, rel)

        self.links.append(new_link)

    def static_link(self, filename, rel=REL_STYLESHEET):
        new_static_link = self.Link(filename, rel, static=True)

        self.links.append(new_static_link)

    def _get_scripts(self):
        return self.scripts

    def _get_links(self):
        return self.links

    def _get_metas(self):
        return self.metas
