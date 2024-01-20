"""Hip Flask extension"""

from flask import url_for
from markupsafe import Markup

class HipExtension:
    """
    Hip Flask extension to simplify CSS and JavaScript integrations
    """

    # Cross origin
    CO_ANONYMOUS = "anonymous"
    CO_USE_CREDENTIALS = "use-credentials"

    class Meta:
        """
        Class to represent a meta tag.

        Attributes
        ----------
        name: str
            name of meta tag
        content: str
            content of meta tag
        http_equiv: bool
            HTTP equiv tag

        Methods
        -------
        as_tag():
            Returns HTML meta tag.
        """

        # Meta name values
        APPLICATION_NAME = "application-name"
        AUTHOR = "author"
        DESCRIPTION = "description"
        GENERATOR = "generator"
        KEYWORDS = "keywords"
        VIEWPORT = "viewport"

        # Meta HTTP equiv
        HE_CONTENT_SP = "content-security-policy"
        HE_CONTENT_TYPE = "content-type"
        HE_DEFAULT_STYLE = "default-style"
        HE_REFRESH = "refresh"

        # Meta name values
        CHARSET = "charset"

        def __init__(self,
                     name,
                     content=None,
                     http_equiv=False):
            self.name = name

            # Explode content if dealing with a list
            if isinstance(content, list):
                self.content = ", ".join(content)
            else:
                self.content = content

            # HTTP equiv tag
            self.http_equiv = http_equiv

            self._cache_meta = None

        def as_tag(self):
            """HTML representation of meta"""

            if self._cache_meta:
                return self._cache_meta

            self._cache_meta = Markup(self._as_tag())
            return self._cache_meta

        def _as_tag(self):
            meta_parts = [ "<meta " ]

            # Build tag, handle charset edge case
            if self.name == self.CHARSET:
                meta_parts.append(f"{self.name}=\"{self.content}\"")
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
        """
        Class to represent a script tag.  

        Attributes
        ----------
        src: str
            Script src
        typ: str
            Script type
        static: bool
            Static URL tag
        asyn: bool
            Async attribute
        defer: bool
            Defer attribute
        nomodule: bool
            Nomodule attribute
        policy: str
            Referrer policy attribute
        priority: str
            Fetch priority attribute
        integrity: str
            Integrity attribute
        crossorigin: str
            Cross origin attribute

        Methods
        -------
        as_tag():
            Returns HTML script tag.
        """

        # Referrer policy
        RP_NO_REFERRER = "no-referrer"
        RP_NO_REFERRER_DOWNGRADE = "no-referrer-when-downgrade"
        RP_ORIGIN = "origin"
        RP_ORIGIN_CROSS_ORIGIN = "origin-when-cross-origin"
        RP_SAME_ORIGIN = "same-origin"
        RP_STRICT_ORIGIN = "strict-origin"
        RP_STRICT_ORIGIN_CROSS_ORIGIN = "strict-origin-when-cross-origin"
        RP_UNSAFE_URL = "unsafe-url"

        # Script type
        TYPE_MIME_JAVASCRIPT = "text/javascript"
        TYPE_IMPORTMAP = "importmap"
        TYPE_MODULE = "module"
        TYPE_SPECULATIONRULES = "speculationrules"

        # Fetch priority
        FP_HIGH = "high"
        FP_LOW = "low"
        FP_AUTO = "auto"

        def __init__(self,
                     src,
                     typ=None,
                     static=False,
                     asyn=False,
                     defer=False,
                     nomodule=False,
                     policy=None,
                     priority=None,
                     integrity=None,
                     crossorigin=None):
            self.src = src
            self.typ = typ
            self.static = static
            self.asyn = asyn
            self.defer = defer
            self.nomodule = nomodule
            self.policy = policy
            self.priority = priority
            self.integrity = integrity
            self.crossorigin = crossorigin

            self._cache_script = None

        def __str__(self):
            return self.src

        def __repr__(self):
            return self.src

        def as_tag(self):
            """HTML represention of script"""

            # Check for cache script tag
            if self._cache_script:
                return self._cache_script

            # Build tag and cache for future calls
            self._cache_script = Markup(self._as_tag())
            return self._cache_script

        def _as_tag(self):
            # Hosting from static URL
            if self.static:
                script_src = url_for('static', filename=self.src)
            else:
                script_src = self.src

            script_parts = [f"<script src=\"{script_src}\""]

            # Type attribute
            if self.typ:
                script_parts.append(f" type=\"{self.typ}\"")

            # Async attribute
            if self.asyn:
                script_parts.append(" async")

            # Defer attribute
            if self.defer:
                script_parts.append(" defer")

            # Nomodule attribute
            if self.nomodule:
                script_parts.append(" nomodule")

            # Referrer policy attribute
            if self.policy:
                script_parts.append(f" referrerpolicy=\"{self.policy}\"")

            # Fetch priority attribute
            if self.priority:
                script_parts.append(f" fetchpriority=\"{self.priority}\"")

            # Integrity attribute
            if self.integrity:
                script_parts.append(f" integrity=\"{self.integrity}\"")

            # Cross origin attribute
            if self.crossorigin:
                script_parts.append(f" crossorigin=\"{self.crossorigin}\"")

            # Close tag
            script_parts.append(f"></script>")

            return "".join(script_parts)

    class Link:
        """
        Class to represent a link tag.  

        Attributes
        ----------
        href: str
            Link href
        rel: str
            Link relelationship
        static: bool
            Static URL tag

        Methods
        -------
        as_tag():
            Returns HTML link tag.
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

        def __init__(self,
                     href,
                     rel,
                     static=False):
            self.href = href
            self.rel = rel
            self.static = static

            self._cache_link = None

        def __str__(self):
            return self.href

        def __repr__(self):
            return self.href

        def as_tag(self):
            """HTML represention of link"""

            if self._cache_link:
                return self._cache_link

            self._cache_link = Markup(self._as_tag())
            return self._cache_link

        def _as_tag(self):
            # Hosting from static URL
            if self.static:
                tag_href = url_for('static', filename=self.href)
            else:
                tag_href = self.href

            # String interpolation
            return f"<link rel=\"{self.rel}\" href=\"{tag_href}\" />"

    def __init__(self, app=None):
        """Initialize extension"""

        self.links = []
        self.scripts = []
        self.metas = []

        self._cache_meta = None

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

        app.jinja_env.globals['macros']['hip_scripts'] = self._get_scripts
        app.jinja_env.globals['macros']['hip_links'] = self._get_links
        app.jinja_env.globals['macros']['hip_metas'] = self._get_metas

    # Functions
    def meta(self,
             name,
             content=None,
             http_equiv=False):
        """Add meta"""

        # Meta tag, http-equiv or normal name=value attributes
        # If name is charset, content is the charset.
        new_meta = self.Meta(name,
                             content=content,
                             http_equiv=http_equiv)

        self.metas.append(new_meta)

    def http_equiv(self,
                   name,
                   content=None):
        """Add meta (http-equiv)"""

        # Meta HTTP equiv tag
        self.meta(name, content=content, http_equiv=True)

    def noscript(self, msg):
        """Add noscript"""

        return f"<noscript>{msg}</noscript>"

    def script(self,
               src,
               typ=None,
               static=False,
               integrity=None,
               crossorigin=None):
        """Add script"""

        # Script (src, type, static URLs or not)
        new_script = self.Script(src,
                                 typ,
                                 static,
                                 integrity=integrity,
                                 crossorigin=crossorigin)

        self.scripts.append(new_script)

    def static_script(self,
                      src,
                      typ=None):
        """Add static script"""

        # Static script
        self.script(src, typ, static=True)

    def link(self,
             href,
             rel=Link.REL_STYLESHEET,
             static=False):
        """Add link"""

        # Link (href, rel, static URLs or not)
        new_link = self.Link(href, rel, static)

        self.links.append(new_link)

    def static_link(self,
                    filename,
                    rel=Link.REL_STYLESHEET):
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
