#!/usr/bin/bash
quarto render README.qmd
sed -i 's#README_files#https://raw.githubusercontent.com/michaeldorman/xplr/master/README_files#g' README.md

