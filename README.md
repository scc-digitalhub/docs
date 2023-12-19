Repository for the documentation of the Digital Hub.

New pages can be created by writing *.md* files. To enable and add a page to the navigation, add the path to your file to the `nav` element in *mkdocs.yml*.

## Install Material for MkDocs
``` shell
pip install mkdocs-material
```

## Run your documentation locally
``` shell
cd user
mkdocs serve
```
The documentation site will be available at *localhost:8000*.

## Deploy the documentation
``` shell
cd user
mkdocs gh-deploy -b gh-pages-user
```
MkDocs will generate the site and automatically push it to the pages branch. It will be available [here](https://scc-digitalhub.github.io/docs/) (changes may take a couple minutes to become effective).

Note that this will generate and update the site even if you didn't commit your `main` changes, but you should always commit them. Otherwise, the next person deploying their updates will undo your changes on the site.

## Dual portal (beta)
The method to build and push the dual portal docs has to be discussed, so for now, unless you specifically need to do this, avoid it. Use the method above instead.

Commit and push your *main* changes, then run the `pages.sh` script:
``` shell
bash pages.sh
```
The script will use MkDocs to build both *user* and *dev* portals, combine the files, checkout to *gh-pages*, commit the updated website and checkout back to *main*.

Since it pushes to the **gh-pages** branch, it has to be configured as the source branch for the docs, which can be done from the repo's page, under *Settings > Pages > Branch*. Once the mode to build the docs has been settled, this will no longer be needed.
