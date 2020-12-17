from json import loads

from pelican import signals
from pelican.contents import Article, Page, Static
from bs4 import BeautifulSoup


def content_object_init(instance):
    if isinstance(instance, (Article, Page, Static)):
        plugin_settings = instance.settings.get("DECORATE_CONTENT", {})
        content_overrides = (
            instance.metadata.get("decorate_content", None)
            if instance.metadata is not None
            else None
        )

        settings = plugin_settings.copy()
        settings.update(
            loads(content_overrides) if content_overrides is not None else {}
        )

        soup = BeautifulSoup(instance._content, "html.parser")

        for selector, class_names in settings.items():
            elems = soup.select(selector)
            for elem in elems:
                elem["class"] = elem.get("class", []) + class_names

        instance._content = soup.decode()


def register():
    signals.content_object_init.connect(content_object_init)
