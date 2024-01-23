#! /bin/bash

set -e

echo "---------------------- Script for GH Pages (sub) ---------------------"
echo "--- Deleting current 'site' folder..."
rm -rf site

echo "--- Building user docs..."
cd user
mkdocs build

echo "--- Building dev docs..."
cd ../dev
mkdocs build -d dev
cd ..

echo "--- Storing files in 'site' folder..."
mv user/site ./site
mv dev/dev site/dev

echo "--- Checking out to gh-pages-alt branch and committing changes..."
git checkout gh-pages-alt
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