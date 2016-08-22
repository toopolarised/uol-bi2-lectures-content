@echo off
pushd ..

del pngs-at-once.md
copy /y NUL pngs-at-once.md >NUL

SET prefix=![]^(./
SET postfix=.png^^)

FOR /R %%I IN (*.png) DO (
	@echo  %prefix%%%~nI%postfix% >> pngs-at-once.md 
)

popd