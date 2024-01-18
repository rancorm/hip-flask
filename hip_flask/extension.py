from flask import url_for, current_app

class HipExtension:
    """
    Hip Flask extension to simplify CSS and JavaScript integrations
    """

    # Relationship type
    REL_ALTERNATE = "alternate"
    REL_AUTHOR = "author"
    REL_DNS_PREFETCH = "dns-prefetch"
    REL_HELP = "help"
    REL_ICON = "icon"
    REL_LICENSE = "license"
    REL_NEXT = "next"
    REL_PINGBACK = "pingback"
    REL_PRECONNECT = "preconnect"
    REL_PREFETCH = "prefetch"
    REL_PRELOAD = "preload"
    REL_PRERENDER = "prerender"
    REL_PREV = "prev"
    REL_SEARCH = "search"
    REL_STYLESHEET = "stylesheet"

    class Meta:
        """Meta tag"""

        def __init__(self, name, content=None, value=None, http_equiv=False):
            self.name = name
            self.content = content
            self.value = value
            self.http_equiv = http_equiv

        def as_tag(self):
            """HTML representation of Meta"""

            meta_parts = [ "<meta " ]

            # Build tag 
            if self.value:
                meta_parts.append(f"{self.name}=\"{self.value}\"")
            else:
                # http-equiv or normal name=value tag
                if self.http_equiv:
                    meta_parts.append(f"http-equiv=\"{self.name}\"")
                else:
                    meta_parts.append(f"name=\"{self.name}\"")

                # Content
                meta_parts.append(f"content=\"{self.content}\"")

            # Close tag
            meta_parts.append(">")

            return "".join(meta_parts)

    class Script:
        """Script tag"""

        def __init__(self, src, static=False):
            self.src = src
            self.static = static

        def __str__(self):
            return self.src

        def __repr__(self):
            return self.src

        def as_tag(self):
            """HTML represention of Script"""

            return f"<script src=\"{self.src}\"></script>"

    class Link:
        """Link tag"""

        def __init__(self, href, rel, static=False):
            self.href = href
            self.rel = rel
            self.static = static

        def __str__(self):
            return self.href

        def __repr__(self):
            return self.href

        def as_tag(self):
            """HTML represention of Link"""

            tag_url = self.href

            if self.static:
                tag_url = url_for('static', filename=self.href)

            return f"<link rel=\"{self.rel}\" href=\"{tag_url}\" />"

    def __init__(self, app=None):
        """Initialize extension"""

        self.links = []
        self.scripts = []
        self.metas = []

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Initialize extension on application"""

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

    def meta(self, name, content=None, value=None):
        """Add meta"""

        new_meta = self.Meta(name, content=content, value=value)

        self.metas.append(new_meta)

    def http_equiv(self, name, content=None):
        """Add meta (http-equiv)"""

        new_meta_http = self.Meta(name, content=content, http_equiv=True)

        self.metas.append(new_meta_http)

    def script(self, src, static=False):
        """Add script"""

        new_script = self.Script(src, static)

        self.scripts.append(new_script)

    def link(self, href, rel=REL_STYLESHEET, static=False):
        """Add link"""

        new_link = self.Link(href, rel, static)

        self.links.append(new_link)

    def static_link(self, filename, rel=REL_STYLESHEET):
        """Add static link"""

        new_static_link = self.Link(filename, rel, static=True)

        self.links.append(new_static_link)

    def _get_scripts(self):
        return self.scripts

    def _get_links(self):
        return self.links

    def _get_metas(self):
        return self.metas
