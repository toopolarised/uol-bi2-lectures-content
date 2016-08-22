@echo off
FOR /R %%I IN (*.pdf) DO (
	echo %%I
	imconvert -density 600 "%%I" -quality 90 "%%~pI%%~nI.png"
)