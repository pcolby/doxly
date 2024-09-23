# SPDX-FileCopyrightText: 2024 Paul Colby <git@colby.id.au>
# SPDX-License-Identifier: GPL-3.0-or-later

"""Convert Doxygen XML to Docusaurus Markdown files."""

import argparse
import logging
import os
import pathlib
import sys

import jinja2

from .doxly import Doxly
from .version import __version__


BUILT_IN_TEMPLATES = [
    'docusaurus'
]


def formatter(prog):
    """Return a wider formatter"""
    return argparse.HelpFormatter(prog, max_help_position=40)


def main():
    """Main CLI entrypoint"""
    parser = argparse.ArgumentParser(
        prog='doxly',
        description='Convert Doxygen XML to Docusaurus Markdown',
        epilog='foo',
        formatter_class=formatter)
    parser.add_argument(
        '-i', '--input-dir', type=pathlib.Path, required=True,
        help='read Doyxgen XML files from DIR', metavar='DIR')
    parser.add_argument(
        '-t', '--template', action='append', type=pathlib.Path, required=True,
        help='read text templates from DIR', metavar='DIR')
    parser.add_argument(
        '-o', '--output-dir', type=pathlib.Path, required=True,
        help='write output files to DIR', metavar='DIR')
    parser.add_argument('-d', '--debug', action='store_true', help='enable debug output')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    args = parser.parse_args()
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
        logging.getLogger(__name__).debug("Debugging enabled")

    print(args.template)
    loaders = []
    for template in args.template:
        if len(template.parts) == 1 and not template.is_dir() and template.parts[0] in BUILT_IN_TEMPLATES:
            loaders.append(jinja2.PackageLoader('doxly', 'templates/' + template.parts[0]))
            print('builtin')
        else:
            loaders.append(jinja2.FileSystemLoader(args.template))
    logging.debug('Template loaders: %s', loaders)
    loader = loaders[0] if len(loaders) == 1 else jinja2.ChoiceLoader(loaders)

    doxly = Doxly(args.input_dir, loader)
    if not doxly.expectedFiles():
        sys.exit(1)
    print(f"About to render {len(doxly.expectedFiles())} files in '{args.output_dir}'")
    os.makedirs(args.output_dir, exist_ok=True)
    doxly.render_files(args.output_dir)

if __name__ == '__main__':
    main()
