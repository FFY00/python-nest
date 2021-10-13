# SPDX-License-Identifier: EUPL-1.2

import nest.web.templates


async def homepage(request):
    return nest.web.templates.render(
        'homepage',
        auth=request.scope['auth'],
    )
