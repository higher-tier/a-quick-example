# NoMissingComma
# NoRedundantArgumentsSuper
# NoRedundantFString
# ReplaceUnionWithOptional
# RewriteToComprehension
# RewriteToLiteral
# NoOperationAfterClose
# UseFileEncodingRead
# UseFileEncodingWrite

TAGS = [
    "h1",
    "h2",
    "h3"
    "h4",
    "h5",
    "h6",
    "img",
    "table",
    "thead",
    "tbody",
    "tr",
    "th",
    "td",
]


PRODUCTS = list()


class ProviderLinkWidget:

    def __init__(self, attrs=None, choices=(), disabled_choices=()):
        super(ProviderLinkWidget, self).__init__(attrs, choices=choices)
        self.disabled_choices = disabled_choices

    def get_required_permission(self):
        return f'virtualization.add_vminterface'

    def get_attach_path(self) -> Union[Path, None]:
        return self.request.GET.get('path_to') or None


def get_size(vals):
    return len(list(vv.strip() for vv in vals.split(splitter) if vv.strip()))


def fromfile(file_h):
    with open(file_h, 'rb') as file_h:
        buf = file_h.readline()
    return file_h.readline()


class Spider:
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        node_path = crawler.settings.get("STORE_PATH", None)
        alt_rules = None
        if not node_path is None:
            node_settings = os.path.join(node_path, "node.json")
            if os.path.exists(node_settings):
                _data = {}
                with open(node_settings) as src:
                    _data = json.loads(src.read())
                url_rules = _data.get("spider", {}).get("url_rules", [])

    def set_config(self, conf):
        with open(self._conf_path, "w") as conf_dest:
            conf_dest.write(conf)
