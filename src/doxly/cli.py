# SPDX-FileCopyrightText: 2024 Paul Colby <git@colby.id.au>
# SPDX-License-Identifier: GPL-3.0-or-later

"""Convert Doxygen XML to Docusaurus Markdown files."""

import argparse
import logging
import pathlib
import sys

from jinja2 import FileSystemLoader

from .doxly import Doxly
from .version import __version__


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
        '-t', '--templates-dir', type=pathlib.Path, required=True,
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

    doxly = Doxly(args.input_dir, FileSystemLoader('/home/paul/src/doxly/templates'))
    print(f"About to render {len(doxly.expectedFiles())} files in ...'")


if __name__ == '__main__':
    main()
