# SPDX-FileCopyrightText: 2024 Paul Colby <git@colby.id.au>
# SPDX-License-Identifier: GPL-3.0-or-later

"""Convert Doxygen XML to Docusaurus Markdown files."""

import json
import logging

import doxmlparser
from jinja2 import Environment, TemplateSyntaxError

from .version import __version__


logger = logging.getLogger(__name__)


class Doxly:
    def __init__(self, doxmlDir, templatesLoader):
        self.context = {
          'doxly': {
              'version':  __version__
          }
        }
        self.doxmlDir = doxmlDir
        self.env = Environment(loader=templatesLoader)
        self.env.filters['kindplural'] = _kind_plural
        self._load_indexes()


    def _load_indexes(self):
        path = self.doxmlDir / 'index.xml'
        logger.debug('Parsing: %s', path)
        try:
            self.context['index'] = doxmlparser.index.parse(path, silence=True)
            logger.debug('Parsed v%s index', self.context['index'].get_version())
        except Exception as e:
            logger.debug(type(e).__name__)
            logger.error('Failed to parse Doxygen XML index file "%s"', path)
            logger.error(e)

        try:
            self.filesIndex = json.loads(self.env.get_template('_index.json').render(self.context))
            logger.debug('Loaded index %s', self.filesIndex)
        except json.decoder.JSONDecodeError as e:
            logger.error("Error JSON-decoding template index: %s", e)
            logger.debug(e.doc)
        except TemplateSyntaxError as e:
            logger.error("Error processing template '%s' at line %d: %s", e.filename, e.lineno, e.message)
        except Exception as e:
            logger.debug(type(e).__name__)
            logger.error("Error processing template index: %s", e)


    def expectedFiles(self):
        return [i['destination'] for i in self.filesIndex]


    def render_files(self):
        logger.debug('Rendering all files...')
        for file in self.filesIndex:
            logger.debug('Rendering:%s', file)
            # if context then setup context.
            #    compoundPath = (dirName / baseName).with_suffix('.xml')
            #    compound = doxmlparser.compound.parse(compoundPath, silence=True)
            # load template; with caching.
            # render

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
