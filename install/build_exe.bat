REM delete old build files
rmdir /s /q build
rmdir /s /q dist

REM build autocanary.exe
pyinstaller install\pyinstaller.spec -y

REM sign autocanary.exe
signtool.exe sign /v /d "AutoCanary" /a /tr http://timestamp.globalsign.com/scripts/timstamp.dll /fd sha256 dist\autocanary\autocanary.exe

REM build an installer, dist\AutoCanary_Setup.exe
makensis.exe install\autocanary.nsi

REM sign OnionShare_Setup.exe
signtool.exe sign /v /d "AutoCanary" /a /tr http://timestamp.globalsign.com/scripts/timstamp.dll /fd sha256 dist\AutoCanary_Setup.exe
