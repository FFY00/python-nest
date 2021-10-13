# SPDX-License-Identifier: EUPL-1.2

import os
import pathlib
import subprocess
import warnings


static_path = pathlib.Path(__file__).absolute().parent
static_files_path = static_path / 'statics'
static_files_path.mkdir(exist_ok=True)

try:
    subprocess.check_call([
        'sassc', '--style=compressed',
        os.fspath(static_path / 'style.scss'),
        os.fspath(static_files_path / 'style.css'),
    ])
except subprocess.CalledProcessError:
    warnings.warn('Could not compile CSS.')
