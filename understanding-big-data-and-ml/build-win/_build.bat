pushd ..
del *.pdf
call build-latex-win/_truncate.bat
call build-latex-win/_compile.bat
call build-latex-win/_topng.bat
call build-latex-win/_truncate.bat
popd
call _truncate.bat
cls