# sitebuilder/views.py
import os
from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.template import Template
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
    return render(request, 'page.html', context )

















































