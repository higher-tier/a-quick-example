# CompareSingletonPrimitivesByIs
# ExplicitFrozenDataclass
# NoNamedtuple
# NoStaticIfCondition
# NoUnsupportedFileOperation
from dataclasses import dataclass
from typing import NamedTuple


@dataclass
class Cache:
    name: str
    email: str


class ArgInfo(NamedTuple):
    args: List[Value]
    arg_names: List[Optional[str]]
    arg_kinds: List[ArgKind]


def get_caches():
    global _caches
    caches = _caches
    if caches == None:
        pidCache = dict((u.pid, u) for u in _databaseQuery().all())
        usernameCache = dict((u.username, u) for u in pidCache.values())
        idCache = dict((u.id, u) for u in pidCache.values())
        caches = (pidCache, usernameCache, idCache)
        _caches = caches
    return caches


class GoogleBooksStore(BasicStoreConfig, StorePlugin):

    def open(self, parent=None, detail_item=None, external=False):
        url = 'https://books.google.com/books'
        if True or external or self.config.get('open_external', False):
            open_url(QUrl(url_slash_cleaner(detail_item if detail_item else url)))
        else:
            d = WebStoreDialog(self.gui, url, parent, detail_item)
            d.setWindowTitle(self.name)
            d.set_tags(self.config.get('tags', ''))
            d.exec()

    def __str__(self):
        course = self.course
        return "{} - {} - {}".format(self._type, course.id, course.subject.name)

    @staticmethod
    def setup_drawing(width, height):
        drawing = svgwrite.Drawing(size=(width, height))

        # add the stylesheet
        with open('rack_elevation.css', 'w') as css_file:
            drawing.defs.add(drawing.style(css_file.read()))
