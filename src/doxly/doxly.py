# SPDX-FileCopyrightText: 2024 Paul Colby <git@colby.id.au>
# SPDX-License-Identifier: GPL-3.0-or-later

"""Convert Doxygen XML to Docusaurus Markdown files."""

import json
import logging

import doxmlparser
from jinja2 import Environment

from .version import __version__


logger = logging.getLogger(__name__)


class Doxly:
    def __init__(self, doxmlDir, templatesLoader):
        self.doxmlDir = doxmlDir
        self.env = Environment(loader=templatesLoader)
        self.env.filters['kindplural'] = _kind_plural
        self._load_doxml_index()


    def _load_doxml_index(self):
        indexPath = self.doxmlDir / 'index.xml'
        logger.debug('Parsing: %s', indexPath)
        index = doxmlparser.index.parse(indexPath, silence=True)
        logger.debug('Parsed v%s index', index.get_version())
        # \todo move base context.
        ctx = {
          'doxly': {
              'version':  __version__
          },
          'index': index,
        }
        template = self.env.get_template('_index.json')
        data = template.render(ctx)
        self.filesIndex = json.loads(data)
        print(data)


    def expectedFiles(self):
        return [i['destination'] for i in self.filesIndex]


def _kind_plural(kind):
    """Return kind as a pural"""
    match kind:
        case 'category':
            return 'categories'
        case 'class':
            return 'classes'
        case 'property':
            return 'properties'
        case _:
            return kind + 's'


# todo remove
def process_compound(dirName, baseName):
    """Process a Doxygen compound"""
    compoundPath = (dirName / baseName).with_suffix('.xml')
    compound = doxmlparser.compound.parse(compoundPath, silence=True)
    for compounddef in compound.get_compounddef():
        # kind = compounddef.get_kind()
        compounddef.get_kind()
        # if kind==DoxCompoundKind.CLASS:
        #     if is_documented(compounddef):
        # elif kind==DoxCompoundKind.STRUCT:
        # elif kind==DoxCompoundKind.UNION:
        # elif kind==DoxCompoundKind.INTERFACE:
        # elif kind==DoxCompoundKind.EXCEPTION:
        # elif kind==DoxCompoundKind.NAMESPACE:
        # elif kind==DoxCompoundKind.FILE:
        #     if is_documented(compounddef):
        # elif kind==DoxCompoundKind.GROUP:
        # elif kind==DoxCompoundKind.PAGE:
        # else:
        #     continue
        # parse_sections(compounddef,metrics)
