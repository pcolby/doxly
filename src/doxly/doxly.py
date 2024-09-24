# SPDX-FileCopyrightText: 2024 Paul Colby <git@colby.id.au>
# SPDX-License-Identifier: GPL-3.0-or-later

"""Convert Doxygen XML to Docusaurus Markdown files."""

import json
import logging

import doxmlparser
import jinja2

from .version import __version__


logger = logging.getLogger(__name__)


class Doxly:
    def __init__(self, doxmlDir, templatesLoader):
        self.doxmlDir = doxmlDir
        self.env = jinja2.Environment(loader=templatesLoader)
        self.env.filters['kindplural'] = _kind_plural
        self.env.globals['doxly'] = {
            'version':  __version__
        }
        self._load_indexes()


    def _load_indexes(self):
        path = self.doxmlDir / 'index.xml'
        logger.debug('Parsing: %s', path)
        try:
            self.env.globals['index'] = doxmlparser.index.parse(path, silence=True)
            logger.debug('Parsed v%s index', self.env.globals['index'].get_version())
        except Exception as e:
            logger.debug(type(e).__name__)
            logger.error('Failed to parse Doxygen XML index file "%s"', path)
            logger.error(e)
            return

        try:
            self.filesIndex = json.loads(self.env.get_template('_index.json').render())
            logger.debug('Loaded index %s', self.filesIndex)
        except json.decoder.JSONDecodeError as e:
            logger.error("Error JSON-decoding template index: %s", e)
            logger.debug(e.doc)
        except jinja2.TemplateNotFound as e:
            logger.error("Failed to find template file '%s'", e.name)
            if isinstance(self.env.loader, jinja2.FileSystemLoader):
                logger.debug("Loader search path: %s", self.env.loader.searchpath)
        except jinja2.TemplateSyntaxError as e:
            logger.error("Error processing template '%s' at line %d: %s", e.filename, e.lineno, e.message)
        except Exception as e:
            logger.debug(type(e).__name__)
            logger.error("Error processing template index: %s", e)


    def expectedFiles(self):
        try:
            return [i['destination'] for i in self.filesIndex]
        except AttributeError:
            return None


    def render_files(self, outputDir):
        logger.debug('Rendering all files...')
        for file in self.filesIndex:
            logger.debug('Rendering:%s', file)
            context = { }
            if 'compound' in file:
                try:
                    compoundPath = (self.doxmlDir / file['compound']).with_suffix('.xml')
                    context['compound'] = doxmlparser.compound.parse(compoundPath, silence=True).get_compounddef()[0]
                except Exception as e:
                    logger.debug(type(e).__name__)
                    logger.error('Failed to parse Doxygen XML compound file "%s"', compoundPath)
                    logger.error(e)
                    return False
            try:
                text = self.env.get_template(file['template']).render(context)
            except jinja2.TemplateNotFound as e:
                logger.error("Failed to find template file '%s'", e.name)
                if isinstance(self.env.loader, jinja2.FileSystemLoader):
                    logger.debug("Loader search path: %s", self.env.loader.searchpath)
                return False
            except jinja2.TemplateSyntaxError as e:
                logger.error("Error processing template '%s' at line %d: %s", e.filename, e.lineno, e.message)
                return False
            except Exception as e:
                logger.debug(type(e).__name__)
                logger.error("Error processing template index: %s", e)
                return False

            with open(outputDir / file['destination'], mode='w') as f:
                f.write(text)
        return True

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
