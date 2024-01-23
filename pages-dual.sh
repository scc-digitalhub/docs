#! /bin/bash

set -e

echo "--------------------- Script for GH Pages (dual) ---------------------"
echo "--- Deleting current 'site' folder..."
rm -rf site
mkdir site

echo "--- Building user docs..."
cd user
mkdocs build -d user

echo "--- Building dev docs..."
cd ../dev
mkdocs build -d dev
cd ..

echo "--- Storing files in 'site' folder..."
mv user/user site/user
mv dev/dev site/dev
cp index.html site/index.html
cp add.css site/add.css

echo "--- Checking out to gh-pages branch and committing changes..."
git checkout gh-pages
cp -r site/* .
rm -r site
echo ".DS_STORE" > .gitignore
git add --all
git commit -m "Updated docs with script"
git push

echo "--- Checking out back to main..."
git checkout main

echo "--- Done."
echo "----------------------------------------------------------------------"