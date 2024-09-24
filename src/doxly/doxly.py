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
        self.env.filters['tomarkdown'] = _to_markdown
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

def _to_markdown(value):
    """Custom filter to convert values to Markdown"""
    logger.debug(f'Converting {type(value).__name__} to Markdown')
    match type(value):
        case doxmlparser.compound.docAnchorType:
            return f'<a id="{value.get_id()}"></a>'
        case doxmlparser.compound.docListItemType:
            #print(value.get_override()) # TODO Not sure what this means.
            #print(value.get_value()) # Same here.
            # TODO we probably need to do hanging indents here?
            return '\n* '+(''.join([ _to_markdown(para) for para in value.get_para() ]))
        case doxmlparser.compound.docListType:
            #print(value.get_type()) # TODO Handle ordered lists?
            #print(value.get_start()) # TODO Handle non-zero starts?
            return ''.join([ _to_markdown(item) for item in value.get_listitem() ])
        case doxmlparser.compound.docMarkupType:
            #print(value.get_ulink()) # TODO
            #print(f'{value.get_computeroutput()}') # TODO
            return ''.join([ _to_markdown(item) for item in value.content_ ])
        case doxmlparser.compound.docParaType:
            return ''.join([ _to_markdown(item) for item in value.content_ ])
        case doxmlparser.compound.docRefTextType:
            content = ''.join([ _to_markdown(item) for item in value.content_ ])
            if value.external:
                logger.debug(f"Ignoring external reference to {value.kindref} '{value.refid}'")
                logger.debug(f"value.external")
                return content
            return f'[{content}]({value.get_refid()})'
        case doxmlparser.compound.docTitleType:
            # todo Bold etc.
            return ''.join([ _to_markdown(item) for item in value.content_ ])
        case doxmlparser.compound.docURLLink:
            content = ''.join([ _to_markdown(item) for item in value.content_ ])
            print(content)
            return f'[{content}]({value.get_url()})'
        case doxmlparser.compound.docVariableListType:
            text = ''
            for entry, item in zip(value.get_varlistentry(), value.get_listitem()):
              text += f'\n## {_to_markdown(entry).strip()}\n'
              text += f'\n{_to_markdown(item).strip()}\n'
            return text
        case doxmlparser.compound.docVarListEntryType:
            return _to_markdown(value.get_term())
        case doxmlparser.compound.docXRefSectType:
            print('TODO xref')
            return 'TODO'
        case doxmlparser.compound.MixedContainer:
            logger.debug(f"MixedContainer:{value.category}:{value.content_type}:'{value.name}':{value.value}")
            match value.getCategory():
                case doxmlparser.compound.MixedContainer.CategoryText:
                    return value.getValue()
                case doxmlparser.compound.MixedContainer.CategorySimple:
                    print("SIMPLE") # Todo
                    return value.getValue()
                case doxmlparser.compound.MixedContainer.CategoryComplex:
                    return _to_markdown(value.getValue())
                case _:
                    logger.warning(f'Unknown MixedContainer category {value.getCategory()}')
                    return value.getValue()
        case _:
            logger.warning(f"Don't know how to convert {value} to Markdown")
            return f'<{type(value).__name__}>'
