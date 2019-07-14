# sitebuilder/management/commands/build.py
import os
import shutil

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.urls import reverse
from django.test.client import Client


def get_pages():
    """
    loop through the ``pages`` dir and
    collect all of our .html files that are located there
    """
    for _name in os.listdir(settings.SITE_PAGES_DIRECTORY):
        if _name.endswith('.html'):
            yield _name[:-5]


class Command(BaseCommand):
    help = 'Build static site output'

    def handle(self, *args, **options):
        """
        Request pages and build output.
        """

        # check if the output dir exists,
        # and if so, removes it to create a clean version
        if os.path.exists(settings.SITE_OUTPUT_DIRECTORY):
            shutil.rmtree(settings.SITE_OUTPUT_DIRECTORY)

        os.mkdir(settings.SITE_OUTPUT_DIRECTORY)
        os.makedirs(settings.STATIC_ROOT)

        # use call_command() to run the ``collectstatic`` command to copy all
        # of the site static resources into the STATIC_ROOT,
        # which is configured to be inside the SITE_OUTPUT_DIRECTORY.
        call_command('collectstatic', interactive=False, clear=True, verbosity=0)
        client = Client()

        # loop and collect
        # all our .html files in pages/
        for _page in get_pages():
            _url = reverse('page', kwargs={'slug': _page})
            response = client.get(_url)
            if _page == 'index':
                output_dir = settings.SITE_OUTPUT_DIRECTORY
            else:
                output_dir = os.path.join(settings.SITE_OUTPUT_DIRECTORY, _page)
                os.makedirs(output_dir)

            # Here is where our templates are rendered as static content.
            # We use Django test client to mimic crawling the site pages and
            # writing the rendered content into the SITE_OUTPUT_DIRECTORY.
            with open(os.path.join(output_dir, 'index.html'), 'wb') as f:
                f.write(response.content)
































