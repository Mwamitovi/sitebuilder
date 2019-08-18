# sitebuilder/views.py
import json
import os
from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.template.loader_tags import BlockNode
from django.template import Template, Context
from django.utils._os import safe_join


def get_page_or_404(name):
    """
    Return page content as a Django template or raise 404 error.
    """
    try:
        file_path = safe_join(settings.SITE_PAGES_DIRECTORY, name)
    except ValueError:
        raise Http404('Page Not found')
    else:
        if not os.path.exists(file_path):
            raise Http404('Page Not Found')

    with open(file_path, 'r') as f:
        page = Template(f.read())

    meta = None

    # loops through the page’s raw nodelist,
    # and check for a BlockNode with the name context.
    # BlockNode is a class definition for creating {% block %} in Django templates.
    # If the context BlockNode is found,
    # we defines a meta-variable for us that contains that content.
    for i, node in enumerate(list(page.nodelist)):
        if isinstance(node, BlockNode) and node.name == 'context':
            meta = page.nodelist.pop(i)
            break

    page._meta = meta
    return page


def page(request, slug='index'):
    """
    Render the requested page if found.
    """
    _file_name = '{}.html'.format(slug)
    _page = get_page_or_404(_file_name)
    context = {
        'slug': slug,
        'page': _page,
    }

    if _page._meta is not None:
        # meta-context is rendered using Python’s json module
        # to convert our { % block context %} into digestible Python
        meta = _page._meta.render(Context())
        extra_context = json.loads(meta)
        context.update(extra_context)

    return render(request, 'page.html', context)
