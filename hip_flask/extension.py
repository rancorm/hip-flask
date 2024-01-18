from flask import url_for, current_app

class HipExtension:
    """
    Hip Flask extension to simplify CSS and JavaScript integrations
    """

    # Meta name values
    META_APPLICATION_NAME = "application-name"
    META_AUTHOR = "author"
    META_DESCRIPTION = "description"
    META_GENERATOR = "generator"
    META_KEYWORDS = "keywords"
    META_VIEWPORT = "viewport"
    

    # Meta HTTP equiv
    META_HE_CONTENT_SP = "content-security-policy"
    META_HE_CONTENT_TYPE = "content-type"
    META_HE_DEFAULT_STYLE = "default-style"
    META_HE_REFRESH = "refresh"

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

    # Referrer policy
    RP_NO_REFERRER = "no-referrer"
    RP_NO_REFERRER_DOWNGRADE = "no-referrer-when-downgrade"
    RP_ORIGIN = "origin"
    RP_ORIGIN_CROSS_ORIGIN = "origin-when-cross-origin"
    RP_SAME_ORIGIN = "same-origin"
    RP_STRICT_ORIGIN = "strict-origin"
    RP_STRICT_ORIGIN_CROSS_ORIGIN = "strict-origin-when-cross-origin"
    RP_UNSAFE_URL = "unsafe-url"

    # Cross origin
    CO_ANONYMOUS = "anonymous"
    CO_USE_CREDENTIALS = "use-credentials"

    # Script type
    TYPE_TEXT_JAVASCRIPT = "text/javascript"


    class Meta:
        """Meta tag"""

        # Meta attributes
        META_CHARSET = "charset"
        
        def __init__(self,
                     name,
                     content=None,
                     value=None,
                     http_equiv=False):
            self.name = name

            # Explode content if dealing with a list
            if type(content) is list:
                self.content = ", ".join(content)
            else:
                self.content = content
            
            self.value = value
            self.http_equiv = http_equiv

        def as_tag(self):
            """HTML representation of meta"""

            meta_parts = [ "<meta " ]

            # Build tag
            if self.value and self.name == self.META_CHARSET:
                meta_parts.append(f"{self.name}=\"{self.value}\"")
            else:
                # http-equiv or normal name=value attributes
                if self.http_equiv:
                    meta_parts.append(f"http-equiv=\"{self.name}\"")
                else:
                    meta_parts.append(f"name=\"{self.name}\"")

                # Add meta content
                meta_parts.append(f"content=\"{self.content}\"")

            # Close tag
            meta_parts.append(">")

            return "".join(meta_parts)

    class Script:
        """Script tag"""

        def __init__(self,
                     src,
                     typ=None,
                     static=False):
            self.src = src
            self.typ = typ
            self.static = static

        def __str__(self):
            return self.src

        def __repr__(self):
            return self.src

        def as_tag(self):
            """HTML represention of script"""

            script_parts = ["<script "]
            
            if self.typ:
                script_parts.append(f"type=\"{self.typ}\" ")

            script_parts.append(f"src=\"{self.src}\"></script>")

            return "".join(script_parts)

    class Link:
        """Link tag"""

        def __init__(self,
                     href,
                     rel,
                     static=False):
            self.href = href
            self.rel = rel
            self.static = static

        def __str__(self):
            return self.href

        def __repr__(self):
            return self.href

        def as_tag(self):
            """HTML represention of link"""

            tag_url = self.href
            
            # Hosting from static URL
            if self.static:
                tag_url = url_for('static', filename=self.href)
            
            # String interpolation
            return f"<link rel=\"{self.rel}\" href=\"{tag_url}\" />"

    def __init__(self, app=None):
        """Initialize extension"""

        self.links = []
        self.scripts = []
        self.metas = []

        if app is not None:
            self._init_app(app)

    def _init_app(self, app):
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

    # Functions
    def meta(self,
             name,
             content=None,
             value=None,
             http_equiv=False):
        """Add meta"""

        # Meta (name=value or "name"=name and "content"=content)
        # http_equiv for
        new_meta = self.Meta(name,
                             content=content,
                             value=value,
                             http_equiv=http_equiv)

        self.metas.append(new_meta)

    def http_equiv(self,
                   name,
                   content=None):
        """Add meta (http-equiv)"""

        # Meta HTTP equiv tag
        self.meta(name, content=content, http_equiv=True)

    def script(self,
               src,
               typ=None,
               static=False):
        """Add script"""
        
        # Script (src, type, static URLs or not)
        new_script = self.Script(src, typ, static)

        self.scripts.append(new_script)

    def static_script(self,
                      src,
                      typ=None):
        """Add static script"""
        
        # Static script
        self.script(src, typ, static=True)

    def link(self,
             href,
             rel=REL_STYLESHEET,
             static=False):
        """Add link"""

        # Link (href, rel, static URLs or not)
        new_link = self.Link(href, rel, static)

        self.links.append(new_link)

    def static_link(self,
                    filename,
                    rel=REL_STYLESHEET):
        """Add static link"""

        # Static link to filename
        self.link(filename, rel, static=True)

    # Internal functions
    def _get_scripts(self):
        return self.scripts

    def _get_links(self):
        return self.links

    def _get_metas(self):
        return self.metas
