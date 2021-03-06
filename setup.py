# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '1.0.13.dev0'

long_description = (
        open('README.txt').read()
        + '\n' +
        'Contributors\n'
        '============\n'
        + '\n' +
        open('CONTRIBUTORS.txt').read()
        + '\n' +
        open('CHANGES.txt').read()
        + '\n')

setup(name='policy.acetterbeek',
        version=version,
        description="policy of ac Etterbeek",
        long_description=long_description,
        # Get more strings from
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        classifiers=[
            "Programming Language :: Python",
            ],
        keywords='',
        author='',
        author_email='',
        url='http://svn.plone.org/svn/collective/',
        license='gpl',
        packages=find_packages('src'),
        package_dir = {'': 'src'},
        namespace_packages=['policy', ],
        include_package_data=True,
        zip_safe=False,
        install_requires=[
            'setuptools',
            'Products.LinguaPlone',
            'webcouturier.dropdownmenu',
            'products.geoloc',
            'collective.quickupload',
            'collective.contentstats',
            'Products.PloneFormGen',
            'quintagroup.analytics',
            'collective.easyslider',
	        'collective.galleriffic',
            'collective.js.galleriffic',
            'Solgema.fullcalendar',
            'collective.ckeditor',
            'collective.gallery',
	        'collective.galleria',
            'plonetheme.acetterbeek',
	        'collective.portlet.videoanysurfer',
            'collective.videoanysurfer',
	        'collective.anysurfer',
            'collective.checktranslated',
            'collective.z3cform.norobots',
            'plone.app.ldap',
            'zest.commentcleanup',
            'cirb.zopemonitoring',
            'plone.app.discussion',
            ],
        extras_require={'test': ['plone.app.testing']},
        entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
