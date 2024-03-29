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

    # Fetch priority
    FP_HIGH = "high"
    FP_LOW = "low"
    FP_AUTO = "auto"

    # Referrer policy
    RP_NO_REFERRER = "no-referrer"
    RP_NO_REFERRER_DOWNGRADE = "no-referrer-when-downgrade"
    RP_ORIGIN = "origin"
    RP_ORIGIN_CO = "origin-when-cross-origin"
    RP_SAME_ORIGIN = "same-origin"
    RP_STRICT_ORIGIN = "strict-origin"
    RP_STRICT_ORIGIN_CO = "strict-origin-when-cross-origin"
    RP_UNSAFE_URL = "unsafe-url"

    class Meta:
        """
        Class to represent a meta tag.

        Attributes
        ----------
        name: str
            name of meta tag
        content: str or list
            content of meta tag
        charset: str
            charset of meta tag
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
        CHARSET_UTF8 = "utf-8"

        def __init__(self,
                     name=None,
                     content=None,
                     charset=None,
                     http_equiv=False):
            self.name = name
            self.charset = charset

            if not self.name and not self.charset:
                raise ValueError("Meta tag must have name or charset")

            # Explode content if dealing with a list
            if isinstance(content, list):
                self.content = ", ".join(content)
            else:
                self.content = content

            # HTTP equiv tag
            self.http_equiv = http_equiv

            self._cache_meta = None

        def __contains__(self, item):
            # Define the logic to check if the item is in the container
            return item is self.name

        def as_tag(self):
            """HTML representation of meta"""

            if self._cache_meta:
                return self._cache_meta

            self._cache_meta = Markup(self._as_tag())
            return self._cache_meta

        def _as_tag(self):
            meta_parts = [ "<meta " ]

            # Build tag parts
            if self.charset:
                meta_parts.append(f"charset=\"{self.charset}\"")
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

        # Script type
        TYPE_JAVASCRIPT = "text/javascript"
        TYPE_IMPORTMAP = "importmap"
        TYPE_MODULE = "module"
        TYPE_SPECULATIONRULES = "speculationrules"

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

        def __contains__(self, item):
            # Define the logic to check if the item is in the container
            return item is self.src

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

            # Handle attributes
            if self.typ:
                script_parts.append(f" type=\"{self.typ}\"")

            if self.asyn:
                script_parts.append(" async")

            if self.defer:
                script_parts.append(" defer")

            if self.nomodule:
                script_parts.append(" nomodule")

            if self.policy:
                script_parts.append(f" referrerpolicy=\"{self.policy}\"")

            if self.priority:
                script_parts.append(f" fetchpriority=\"{self.priority}\"")

            if self.integrity:
                script_parts.append(f" integrity=\"{self.integrity}\"")

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
        rel: str or list
            Link relelationship
        static: bool
            Static URL tag
        a: str
            As attribute
        typ: str
            Type attribute (recommended practice is to omit)
        policy: str
            Referrer policy attribute
        priority: str
            Fetch priority attribute
        integrity: str
            Integrity attribute
        crossorigin: str
            Cross origin attribute
        sizes: str
            Sizes attribute
        media: str
            Media attribute
        disabled: bool
            Disabled attribute

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
        REL_CANONICAL = "canonical"
        REL_MANIFEST = "manifest"
        REL_ME = "me"
        REL_MODULE_PRELOAD = "modulepreload"
        REL_PRIVACY_POLICY = "privacy-policy"
        REL_TERMS_OF_SERVICE = "terms-of-service"
        REL_TOS = REL_TERMS_OF_SERVICE

        # As type
        AS_AUDIO = "audio"
        AS_DOCUMENT = "document"
        AS_EMBED = "embed"
        AS_FETCH = "fetch"
        AS_FONT = "font"
        AS_IMAGE = "image"
        AS_OBJECT = "object"
        AS_SCRIPT = "script"
        AS_STYLE = "style"
        AS_TRACK = "track"
        AS_VIDEO = "video"
        AS_WORKER = "worker"

        # Link type
        TYPE_ATOM = "application/atom+xml"
        TYPE_HTML = "text/html"
        TYPE_CSS = "text/css"
        TYPE_RSS = "application/rss+xml"
        TYPE_PDF = "application/pdf"
        TYPE_PNG = "image/png"
        TYPE_JPEG = "image/jpeg"
        TYPE_GIF = "image/gif"
        TYPE_SVG = "image/svg+xml"
        TYPE_WOFF2 = "font/woff2"

        # Blocking operations
        BLOCK_RENDER = "render"

        def __init__(self,
                     href,
                     rel,
                     static=False,
                     a=None,
                     typ=None,
                     policy=None,
                     priority=None,
                     integrity=None,
                     crossorigin=None,
                     sizes=None,
                     media=None,
                     lang=None,
                     title=None,
                     block=None,
                     disabled=False):
            self.href = href

            # Explode rel if dealing with a list
            if isinstance(rel, list):
                self.rel = " ".join(rel)
            else:
                self.rel = rel

            self.static = static
            self.a = a 
            self.typ = typ
            self.policy = policy
            self.priority = priority
            self.crossorigin = crossorigin
            self.integrity = integrity
            self.sizes = sizes
            self.media = media

            # Values for hreflang attribute are specified using language tags as
            # defined in BCP 47
            self.lang = lang
            self.title = title

            # Explode block if dealing with a list
            if isinstance(block, list):
                self.block = " ".join(block)
            else:
                self.block = block

            self.disabled = disabled

            # Check for preload and as attribute
            if (rel == self.REL_PRELOAD) and not self.a:
                raise ValueError("Preload link must have 'as' attribute")

            # Hreflang requires ref attribute
            if self.lang and not self.ref:
                raise ValueError("Lang must have ref attribute")

            self._cache_link = None

        def __str__(self):
            return self.href

        def __repr__(self):
            return self.href

        def __contains__(self, item):
            # Define the logic to check if the item is in the container
            return item is self.href

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

            link_parts = [f"<link href=\"{tag_href}\" rel=\"{self.rel}\""]

            # As attribute (preload and modulepreload)
            if self.a and self.rel == self.REL_PRELOAD:
                link_parts.append(f" as=\"{self.a}\"")
            elif self.a and self.rel == self.REL_MODULE_PRELOAD:
                link_parts.append(f" as=\"{self.a}\"")

            # Handle attributes
            if self.typ:
                link_parts.append(f" type=\"{self.typ}\"")

            if self.crossorigin:
                link_parts.append(f" crossorigin=\"{self.crossorigin}\"")

            if self.integrity:
                link_parts.append(f" integrity=\"{self.integrity}\"")

            if self.policy:
                link_parts.append(f" referrerpolicy=\"{self.policy}\"")

            if self.priority:
                link_parts.append(f" fetchpriority=\"{self.priority}\"")

            if self.sizes:
                link_parts.append(f" sizes=\"{self.sizes}\"")

            if self.media:
                link_parts.append(f" media=\"{self.media}\"")

            if self.lang:
                link_parts.append(f" hreflang=\"{self.lang}\"")

            if self.title:
                link_parts.append(f" title=\"{self.title}\"")

            if self.block:
                link_parts.append(f" block=\"{self.block}\"")

            if self.disabled:
                link_parts.append(" disabled")

            # Close tag
            link_parts.append(" />")

            return "".join(link_parts)

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

        # Add macros to Jinja globals
        if 'macros' not in app.jinja_env.globals:
            app.jinja_env.globals['macros'] = {}

        # Register macros
        app.jinja_env.globals['macros']['hip_scripts'] = self._get_scripts
        app.jinja_env.globals['macros']['hip_links'] = self._get_links
        app.jinja_env.globals['macros']['hip_metas'] = self._get_metas

    # Functions
    def meta(self,
             name=None,
             content=None,
             charset=None,
             http_equiv=False):
        """Add meta"""

        new_meta = self.Meta(name,
                             content,
                             charset,
                             http_equiv)

        self.metas.append(new_meta)

    def http_equiv(self,
                   name,
                   content=None):
        """Add meta (http-equiv)"""

        # Meta HTTP equiv tag
        self.meta(name,
                  content,
                  True)

    def noscript(self, msg):
        """Add noscript"""

        return f"<noscript>{msg}</noscript>"

    def script(self,
               src,
               typ=None,
               static=False,
               asyn=False,
               defer=False,
               policy=None,
               priority=None,
               integrity=None,
               crossorigin=None):
        """Add script"""

        # Script
        new_script = self.Script(src,
                                 typ,
                                 static,
                                 asyn,
                                 defer,
                                 policy,
                                 priority,
                                 integrity,
                                 crossorigin)

        self.scripts.append(new_script)

    def static_script(self,
                      src,
                      typ=None,
                      asyn=False,
                      defer=False,
                      policy=None,
                      priority=None,
                      integrity=None,
                      crossorigin=None):
        """Add static script"""

        # Static script
        self.script(src,
                    typ,
                    True,
                    asyn,
                    defer,
                    policy,
                    priority,
                    integrity,
                    crossorigin)

    def link(self,
             href,
             rel=Link.REL_STYLESHEET,
             static=False,
             a=None,
             typ=None,
             policy=None,
             priority=None,
             integrity=None,
             crossorigin=None,
             sizes=None,
             media=None,
             lang=None,
             title=None,
             block=None,
             disabled=False):
        """Add link"""

        # Link
        new_link = self.Link(href,
                             rel,
                             static,
                             a,
                             typ,
                             policy,
                             priority,
                             integrity,
                             crossorigin,
                             sizes,
                             media,
                             lang,
                             title,
                             block,
                             disabled)

        self.links.append(new_link)

    def static_link(self,
                    filename,
                    rel=Link.REL_STYLESHEET,
                    a=None,
                    typ=None,
                    policy=None,
                    priority=None,
                    integrity=None,
                    crossorigin=None,
                    sizes=None,
                    media=None,
                    lang=None,
                    title=None,
                    block=None,
                    disabled=False):
        """Add static link"""

        # Static Link
        self.link(filename,
                  rel,
                  True,
                  a,
                  typ,
                  policy,
                  priority,
                  integrity,
                  crossorigin,
                  sizes,
                  media,
                  lang,
                  title,
                  block,
                  disabled)

    # Internal functions
    def _get_scripts(self):
        return self.scripts

    def _get_links(self):
        return self.links

    def _get_metas(self):
        return self.metas
