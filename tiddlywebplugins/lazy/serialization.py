"""
Serialize into a tiddlywiki wiki, leaving out most of the tiddlers
so they can be loaded later by something else.

The missing tiddlers are placed in a tiddler called LazyTiddlers.
"""

from tiddlywebwiki.serialization import (
        Serialization as WikiSerialization, MARKUPS)


from tiddlyweb.model.tiddler import Tiddler
from tiddlyweb.web.util import server_base_url, encode_name

ACTIVE_TITLES = [
        'DefaultTiddlers',
        'MainMenu',
        'WindowTitle',
        'SiteTitle',
        'SiteSubtitle',
        ]

FRAGMENTS = [
        'Commands',
        'Template',
        'StyleSheet',
        ]

TAGS = [
        'systemConfig',
        'excludeLists',
        'systemTheme',
        ]

BAGS = [
        'system',
        ]

class Serialization(WikiSerialization):

    def _create_tiddlers(self, title, tiddlers):
        """
        Figure out the content to be pushed into the
        wiki and calculate the title.
        """
        saves = []
        lines = []
        window_title = None
        candidate_title = None
        candidate_subtitle = None
        markup_tiddlers = MARKUPS.keys()
        found_markup_tiddlers = {}
        tiddler_count = 0
        for tiddler in tiddlers:
            if self._lazy_eligible(tiddler):
                saves.append(tiddler)
            else:
                lines.append(self._tiddler_as_div(tiddler))
            tiddler_title = tiddler.title
            if tiddler_title == 'WindowTitle':
                window_title = tiddler.text
            if tiddler_title == 'SiteTitle':
                candidate_title = tiddler.text
            if tiddler_title == 'SiteSubtitle':
                candidate_subtitle = tiddler.text
            if tiddler_title in markup_tiddlers:
                found_markup_tiddlers[tiddler_title] = tiddler.text
            tiddler_count += 1

        if tiddler_count == 1:
            default_tiddler = Tiddler('DefaultTiddlers', '_virtual')
            default_tiddler.text = '[[' + tiddler.title + ']]'
            lines.append(self._tiddler_as_div(default_tiddler))

        if saves:
            save_tiddler = Tiddler('LazyTiddlers', '_virtual')
            save_tiddler.text = '\n'.join(['%s:%s' %
                (tiddler.bag, tiddler.title) for tiddler in saves])
            lines.append(self._tiddler_as_div(save_tiddler))

        browsable_url = None
        try:
            if tiddler.recipe:
                workspace = '/recipes/%s/tiddlers' % encode_name(tiddler.recipe)
            else:
                workspace = '/bags/%s/tiddlers' % encode_name(tiddler.bag)
            browsable_url = server_base_url(self.environ) + workspace
        except UnboundLocalError:
            pass # tiddler is not set because tiddlers was empty

        # Turn the title into HTML and then turn it into
        # plain text so it is of a form satisfactory to <title>
        title = self._determine_title(title, window_title, candidate_title,
                candidate_subtitle)
        title = self._plain_textify_string(title)

        return browsable_url, lines, title, found_markup_tiddlers

    def _lazy_eligible(self, tiddler):
        for bag in BAGS:
            if bag == tiddler.bag:
                return False
        for tag in TAGS:
            if tag in tiddler.tags:
                return False
        for fragment in FRAGMENTS:
            if fragment in tiddler.title:
                return False
        special_titles = self.environ['tiddlyweb.config'].get('lazy.titles', [])
        if tiddler.title in special_titles + ACTIVE_TITLES + MARKUPS.keys():
            return False
        return True
