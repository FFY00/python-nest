# SPDX-License-Identifier: EUPL-1.2

import pathlib

import mako.exceptions
import mako.lookup

from starlette.responses import HTMLResponse

import nest.web


templates_path = pathlib.Path(__file__).absolute().parent
templates = mako.lookup.TemplateLookup(directories=[
    templates_path,
])


def render(template, **render_params) -> str:
    try:
        return HTMLResponse(
            templates.get_template(
                f'{template}.html'
            ).render(
                url=nest.web.WEBSITE_URL,
                **render_params,
            ),
        )
    except Exception:
        if not nest.web.DEBUG:
            raise
        return HTMLResponse(
            mako.exceptions.html_error_template().render(),
            status_code=500,
        )
