[![Join us on Slack](https://cldup.com/jWUT4QFLnq.png)](https://devopspathfinder.slack.com/messages/C915T1NEP)

ckanext-bcgov-cli
=============

This extension provides the cli customized features on the [BC Data Catalogue](http://catalogue.data.gov.bc.ca), such as creating vocab or organizations via paster

Installation
============

1.  Activate virtual environment, e.g.

        $ . /usr/lib/ckan/default/bin/activate

2.  Install the extension. Switch to `ckanext-bcgov-cli` extension directory and run the following command:

        python setup.py develop

3.  Create default vocabularies

        cd ckanext-bcgov-cli/ckanext/bcgov/cli/scripts
        $ python create_vocabs.py

   Note: The following data files in `ckanext-bcgov-cli/ckanext/bcgov/cli/scripts/data` is required:

        edc-vocabs.json

4.  Create organizations

        $ cd ckanext-bcgov-cli/ckanext/bcgov/cli/scripts
        $ python create_orgs.py

   Note: The following data files in `ckanext-bcgov/ckanext/bcgov/cli/scripts/data` is required:

        org_suborg_sector_mapping_forEDC.csv


    Original Repo Copyright 2018, Province of British Columbia.
