REM build the exe
python setup.py py2exe

REM sign autocanary.exe
signtool.exe sign /v /d "AutoCanary" /a /tr "http://www.startssl.com/timestamp" dist\autocanary.exe

REM build an installer, dist\AutoCanary_Setup.exe
makensisw install\autocanary.nsi

REM sign AutoCanary_Setup.exe
signtool.exe sign /v /d "AutoCanary" /a /tr "http://www.startssl.com/timestamp" dist\AutoCanary_Setup.exe
