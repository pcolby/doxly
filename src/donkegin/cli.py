# SPDX-FileCopyrightText: 2024 Paul Colby <git@colby.id.au>
# SPDX-License-Identifier: GPL-3.0-or-later

"""Convert Doxygen XML to Docusaurus Markdown files."""

import argparse
import pathlib

from .render import process_index


def main():
    """Main CLI entrypoint"""
    parser = argparse.ArgumentParser(
        description='Convert Doxygen XML to Docusaurus Markdown',
        epilog='foo')
    parser.add_argument('-d', '--debug', action='store_true', help="enable debugging")
    parser.add_argument(
        '-i', '--doxml', type=pathlib.Path, required=True,
        help='Doxygen XML directory', metavar='DIR')
    parser.add_argument(
        '-o', '--output', type=pathlib.Path, required=True,
        help='utput directory', metavar='DIR')
    args = parser.parse_args()
    # if args.debug:
    #     logger.setLevel(logging.DEBUG)
    process_index(args.doxml)
    print("done")


if __name__ == '__main__':
    main()
