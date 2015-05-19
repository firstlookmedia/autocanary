REM build the exe
python setup.py py2exe

REM sign autocanary.exe
signtool.exe sign /v /d "AutoCanary" /a /tr http://timestamp.globalsign.com/scripts/timstamp.dll dist\autocanary.exe

REM build an installer, dist\AutoCanary_Setup.exe
makensisw install\autocanary.nsi

REM sign AutoCanary_Setup.exe
signtool.exe sign /v /d "AutoCanary" /a /tr http://timestamp.globalsign.com/scripts/timstamp.dll dist\AutoCanary_Setup.exe
