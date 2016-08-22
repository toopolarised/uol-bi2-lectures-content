pushd ..
del *.pdf
call build-win/_truncate.bat
call build-win/_compile.bat
call build-win/_topng.bat
call build-win/_truncate.bat
popd
call _truncate.bat
cls