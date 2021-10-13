# SPDX-License-Identifier: EUPL-1.2

import asgi_auth_github

from starlette.applications import Starlette
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles

import nest.web
import nest.web.static
import nest.web.templates

from nest.web import routes


original_app = Starlette(
    debug=nest.web.DEBUG,
    routes=[
        Mount('/static', StaticFiles(packages=['nest.web.static'])),
        Route('/', routes.homepage),
    ],
)


authenticated_app = asgi_auth_github.GitHubAuth(
    original_app,
    client_id=nest.web.GITHUB_CLIENT_ID,
    client_secret=nest.web.GITHUB_CLIENT_SECRET,
    require_auth=False,
)

app = authenticated_app
