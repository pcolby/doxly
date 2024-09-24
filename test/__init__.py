# SPDX-FileCopyrightText: 2024 Paul Colby <git@colby.id.au>
# SPDX-License-Identifier: GPL-3.0-or-later

import os.path
import sys

# Add our project's `src` directory to the start of the import path.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))
