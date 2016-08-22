@echo off
echo 'Compiling LaTex to PDF. Please, wait ...'
latexmk -pdf -shell-escape
echo 'Ending...'