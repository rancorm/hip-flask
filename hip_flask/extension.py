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

    class Style:
        def __init__(self, href):
            self.href = href

        def __str__(self):
            return self.href

        def __repr__(self):
            return self.href

        def as_tag(self):
            return f"<link rel=\"stylesheet\" href=\"{self.href}\" />"

    def __init__(self, app=None):
        self.stylesheets = []
        self.scripts = []

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
        app.jinja_env.globals['macros']['styles'] = self._get_styles

    def script(self, url):
        script = self.Script(url)
        self.scripts.append(script)

    def style(self, url):
        style = self.Style(url)
        self.stylesheets.append(style)

    def _get_scripts(self):
        return self.scripts

    def _get_styles(self):
        return self.stylesheets

