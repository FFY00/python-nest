# SPDX-License-Identifier: EUPL-1.2

from starlette.applications import Starlette
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles

import nest.web
import nest.web.static
import nest.web.templates

from nest.web import routes


app = Starlette(
    debug=nest.web.DEBUG,
    routes=[
        Mount('/static', StaticFiles(packages=['nest.web.static'])),
        Route('/', routes.homepage),
    ],
)
