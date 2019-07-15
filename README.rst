
Rapid Prototyping
=================

To create a successful product, 
it is vital that designers and developers can work effectively side by side.
While choosing the best framework is a key part of starting any project, 
deciding on the proper workflow is also a priority.

Lately, alot of teams are working "asychronously" more so if distributed.
Django can enable both parties (designers and developers) to utilize parts of 
the framework that they need to get started, right away.

In this project, we embark on creating a static site app with Django framework.
We make use of Django’s flexible templating, management command abstractions,
and community extensions such as the django-compressor.


## IMPORTANT

** These are the tools used: (but you are not limited)
   - Python: 3.6.3 (core language)
   - Django: 1.11.6 (web Framework)
   - django-compressor: 2.3 (compress/minify css & js files)
   - Semantic-UI: 2.4.0 (css library)
   - JSON (JavaScript Pbject Notation)


## Get Started


- Create the module, "sitebuilder/Prototypes.py" and define minimal settings for our project.
  Note that we are following the minimalist approach to working with Django projects.
  ** For production projects, always remember to turn DEBUG off, and store SECRET_KEY privately.

- Within "sitebuilder/sitebuilder", 
  create urls.py, views.py and folders (templates and static).
  This is where the other key project modules/files are defined.
  ** Notice that both our urlpatterns route to the page() view function.
  ** And we define get_page_or_404(), called by page(), to return page content as Template.  

- Create "sitebuilder/pages", and add the Prototypes layout and navigation templates here.
  These templates will be rendered as included within the page.html template.

- Create a management command within mmodule "sitebuilder/management/commands/build.py",
  and we define Command() to build our html templates that we shall serve.

- Add django-compressor configurations to ``settings.configure`` within prototype.py module.
  Update build.Command with settings.COMPRESS_ENABLED and call_command() to compress.
  
- Refactor the base.html template.
  ** Enclose the css- and js-files referenced with the "compress" css- and js-blocks.

- Run this command within the root folder, ``/sitebuilder > python prototypes.py build``.
  ** Note that this command will auto-create the folder we specified as SITE_OUTPUT_DIRECTORY,
     as specified within prototypes.settings.configure().

- Switch to the generated build/ folder, ``/_build > python -m http.server 9000``.
  If you do not specify a port, your files will be served at port 8000.


### Reference

- Working light with django: (http://www.oreilly.com/catalog/0636920032502)
- See more about django: (https://docs.djangoproject.com/en/dev/releases/1.11/)
- See django-compressor: (http://django-compressor.readthedocs.org/en/develop/settings/)
- Explore Semantic UI: http://www.semantic-ui.com/


### Contribution guidelines
   - Extend the prototype to be RESTful
   - Other guidelines shall be issued with time.

### Who i talk to?
   - Contact: @MwamiTovi on GitHub
   - Email directly: matovu.synergy@gmail.com
