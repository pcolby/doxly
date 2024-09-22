# SPDX-FileCopyrightText: 2024 Paul Colby <git@colby.id.au>
# SPDX-License-Identifier: GPL-3.0-or-later

"""Convert Doxygen XML to Docusaurus Markdown files."""

import json
import logging

import doxmlparser
import jinja2 as j2

from ._version import __version__


logger = logging.getLogger(__name__)
env = j2.Environment(loader=j2.FileSystemLoader('/home/paul/src/doxly/templates'))


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


def process_index(doxmlDir):
    """Process a Doxygen index"""
    indexPath = doxmlDir / 'index.xml'
    logger.debug('Parsing: %s', indexPath)
    index = doxmlparser.index.parse(indexPath, silence=True)
    logger.debug('Parsed v%s index', index.get_version())
    for compound in index.get_compound():
        logger.debug("%s %s", compound.get_kind(), compound.get_refid())
        # process_compound(doxmlDir, compound.get_refid())
    ctx = {
      'doxly': { 'version':  __version__ },
      'index': index,
    }
    template = env.get_template('_index.json')
    data = template.render(ctx)
    #print(data)
    j = json.loads(data)
    print(j)
    print('About to render %d files in ...' % (len(j)))
