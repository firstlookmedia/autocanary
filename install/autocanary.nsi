!define APPNAME "AutoCanary"
!define BINPATH "..\dist\autocanary"

# change these with each release
!define INSTALLSIZE 37392
!define VERSIONMAJOR 0
!define VERSIONMINOR 2
!define VERSIONSTRING "0.2.1"

RequestExecutionLevel admin

Name "AutoCanary"
InstallDir "$PROGRAMFILES\${APPNAME}"
Icon "icon.ico"

!include LogicLib.nsh

Page directory
Page instfiles

!macro VerifyUserIsAdmin
UserInfo::GetAccountType
pop $0
${If} $0 != "admin" ;Require admin rights on NT4+
    messageBox mb_iconstop "Administrator rights required!"
    setErrorLevel 740 ;ERROR_ELEVATION_REQUIRED
    quit
${EndIf}
!macroend

# in order to code sign uninstall.exe, we need to do some hacky stuff outlined
# here: http://nsis.sourceforge.net/Signing_an_Uninstaller
!ifdef INNER
    !echo "Creating uninstall.exe"
    OutFile "$%TEMP%\tempinstaller.exe"
    SetCompress off
!else
    !echo "Creating normal installer"
    !system "$\"${NSISDIR}\makensis$\" /DINNER autocanary.nsi" = 0
    !system "$%TEMP%\tempinstaller.exe" = 2
    !system "signtool.exe sign /v /d $\"Uninstall AutoCanary$\" /a /tr http://timestamp.globalsign.com/scripts/timstamp.dll $%TEMP%\uninstall.exe" = 0

    # all done, now we can build the real installer
    OutFile "..\dist\AutoCanary_Setup.exe"
    SetCompressor /FINAL /SOLID lzma
!endif

Function .onInit
    !ifdef INNER
        WriteUninstaller "$%TEMP%\uninstall.exe"
        Quit # bail out early
    !endif

    setShellVarContext all
    !insertmacro VerifyUserIsAdmin
FunctionEnd

Section "install"
    SetOutPath "$INSTDIR"
    File "icon.ico"
    File "${BINPATH}\api-ms-win-core-console-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-core-datetime-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-core-debug-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-core-errorhandling-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-core-file-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-core-file-l1-2-0.dll"
    File "${BINPATH}\api-ms-win-core-file-l2-1-0.dll"
    File "${BINPATH}\api-ms-win-core-handle-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-core-heap-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-core-interlocked-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-core-libraryloader-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-core-localization-l1-2-0.dll"
    File "${BINPATH}\api-ms-win-core-memory-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-core-namedpipe-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-core-processenvironment-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-core-processthreads-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-core-processthreads-l1-1-1.dll"
    File "${BINPATH}\api-ms-win-core-profile-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-core-rtlsupport-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-core-string-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-core-synch-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-core-synch-l1-2-0.dll"
    File "${BINPATH}\api-ms-win-core-sysinfo-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-core-timezone-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-core-util-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-crt-conio-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-crt-convert-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-crt-environment-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-crt-filesystem-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-crt-heap-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-crt-locale-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-crt-math-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-crt-multibyte-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-crt-process-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-crt-runtime-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-crt-stdio-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-crt-string-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-crt-time-l1-1-0.dll"
    File "${BINPATH}\api-ms-win-crt-utility-l1-1-0.dll"
    File "${BINPATH}\autocanary.exe"
    File "${BINPATH}\autocanary.exe.manifest"
    File "${BINPATH}\base_library.zip"
    File "${BINPATH}\MSVCP140.dll"
    File "${BINPATH}\MSVCR100.dll"
    File "${BINPATH}\pyexpat.pyd"
    File "${BINPATH}\PyQt5.Qt.pyd"
    File "${BINPATH}\PyQt5.QtCore.pyd"
    File "${BINPATH}\PyQt5.QtGui.pyd"
    File "${BINPATH}\PyQt5.QtPrintSupport.pyd"
    File "${BINPATH}\PyQt5.QtWidgets.pyd"
    File "${BINPATH}\python3.dll"
    File "${BINPATH}\python35.dll"
    File "${BINPATH}\pywintypes35.dll"
    File "${BINPATH}\Qt5Core.dll"
    File "${BINPATH}\Qt5Gui.dll"
    File "${BINPATH}\Qt5PrintSupport.dll"
    File "${BINPATH}\Qt5Svg.dll"
    File "${BINPATH}\Qt5Widgets.dll"
    File "${BINPATH}\select.pyd"
    File "${BINPATH}\sip.pyd"
    File "${BINPATH}\ucrtbase.dll"
    File "${BINPATH}\unicodedata.pyd"
    File "${BINPATH}\VCRUNTIME140.dll"
    File "${BINPATH}\win32process.pyd"
    File "${BINPATH}\_bz2.pyd"
    File "${BINPATH}\_ctypes.pyd"
    File "${BINPATH}\_hashlib.pyd"
    File "${BINPATH}\_lzma.pyd"
    File "${BINPATH}\_socket.pyd"
    File "${BINPATH}\_ssl.pyd"

    SetOutPath "$INSTDIR\share"
    File "${BINPATH}\share\icon.png"
    File "${BINPATH}\share\version"

    SetOutPath "$INSTDIR\qt5_plugins\iconengines"
    File "${BINPATH}\qt5_plugins\iconengines\qsvgicon.dll"

    SetOutPath "$INSTDIR\qt5_plugins\imageformats"
    File "${BINPATH}\qt5_plugins\imageformats\qgif.dll"
    File "${BINPATH}\qt5_plugins\imageformats\qicns.dll"
    File "${BINPATH}\qt5_plugins\imageformats\qico.dll"
    File "${BINPATH}\qt5_plugins\imageformats\qjpeg.dll"
    File "${BINPATH}\qt5_plugins\imageformats\qsvg.dll"
    File "${BINPATH}\qt5_plugins\imageformats\qtga.dll"
    File "${BINPATH}\qt5_plugins\imageformats\qtiff.dll"
    File "${BINPATH}\qt5_plugins\imageformats\qwbmp.dll"
    File "${BINPATH}\qt5_plugins\imageformats\qwebp.dll"

    SetOutPath "$INSTDIR\qt5_plugins\platforms"
    File "${BINPATH}\qt5_plugins\platforms\qminimal.dll"
    File "${BINPATH}\qt5_plugins\platforms\qoffscreen.dll"
    File "${BINPATH}\qt5_plugins\platforms\qwindows.dll"

    SetOutPath "$INSTDIR\qt5_plugins\printsupport"
    File "${BINPATH}\qt5_plugins\printsupport\windowsprintersupport.dll"

    # uninstaller
    !ifndef INNER
        SetOutPath $INSTDIR
        File $%TEMP%\uninstall.exe
    !endif

    # start menu
    CreateShortCut "$SMPROGRAMS\${APPNAME}.lnk" "$INSTDIR\autocanary.exe" "" "$INSTDIR\icon.ico"

    # registry information for add/remove programs
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "DisplayName" "${APPNAME}"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "UninstallString" "$\"$INSTDIR\uninstall.exe$\""
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "QuietUninstallString" "$\"$INSTDIR\uninstall.exe$\" /S"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "InstallLocation" "$\"$INSTDIR$\""
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "DisplayIcon" "$\"$INSTDIR\icon.ico$\""
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "DisplayVersion" ${VERSIONSTRING}
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "VersionMajor" ${VERSIONMAJOR}
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "VersionMinor" ${VERSIONMINOR}
    # there is no option for modifying or repairing the install
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "NoModify" 1
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "NoRepair" 1
    # set the INSTALLSIZE constant (!defined at the top of this script) so Add/Remove Programs can accurately report the size
    WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "EstimatedSize" ${INSTALLSIZE}
SectionEnd

# uninstaller
Function un.onInit
    SetShellVarContext all

    #Verify the uninstaller - last chance to back out
    MessageBox MB_OKCANCEL "Uninstall ${APPNAME}?" IDOK next
        Abort
    next:
    !insertmacro VerifyUserIsAdmin
FunctionEnd

!ifdef INNER
    Section "uninstall"
        Delete "$SMPROGRAMS\${APPNAME}.lnk"

        # remove files
        Delete "$INSTDIR\api-ms-win-core-console-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-core-datetime-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-core-debug-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-core-errorhandling-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-core-file-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-core-file-l1-2-0.dll"
        Delete "$INSTDIR\api-ms-win-core-file-l2-1-0.dll"
        Delete "$INSTDIR\api-ms-win-core-handle-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-core-heap-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-core-interlocked-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-core-libraryloader-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-core-localization-l1-2-0.dll"
        Delete "$INSTDIR\api-ms-win-core-memory-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-core-namedpipe-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-core-processenvironment-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-core-processthreads-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-core-processthreads-l1-1-1.dll"
        Delete "$INSTDIR\api-ms-win-core-profile-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-core-rtlsupport-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-core-string-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-core-synch-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-core-synch-l1-2-0.dll"
        Delete "$INSTDIR\api-ms-win-core-sysinfo-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-core-timezone-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-core-util-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-crt-conio-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-crt-convert-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-crt-environment-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-crt-filesystem-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-crt-heap-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-crt-locale-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-crt-math-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-crt-multibyte-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-crt-process-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-crt-runtime-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-crt-stdio-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-crt-string-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-crt-time-l1-1-0.dll"
        Delete "$INSTDIR\api-ms-win-crt-utility-l1-1-0.dll"
        Delete "$INSTDIR\autocanary.exe"
        Delete "$INSTDIR\autocanary.exe.manifest"
        Delete "$INSTDIR\base_library.zip"
        Delete "$INSTDIR\MSVCP140.dll"
        Delete "$INSTDIR\MSVCR100.dll"
        Delete "$INSTDIR\pyexpat.pyd"
        Delete "$INSTDIR\PyQt5.Qt.pyd"
        Delete "$INSTDIR\PyQt5.QtCore.pyd"
        Delete "$INSTDIR\PyQt5.QtGui.pyd"
        Delete "$INSTDIR\PyQt5.QtPrintSupport.pyd"
        Delete "$INSTDIR\PyQt5.QtWidgets.pyd"
        Delete "$INSTDIR\python3.dll"
        Delete "$INSTDIR\python35.dll"
        Delete "$INSTDIR\pywintypes35.dll"
        Delete "$INSTDIR\Qt5Core.dll"
        Delete "$INSTDIR\Qt5Gui.dll"
        Delete "$INSTDIR\Qt5PrintSupport.dll"
        Delete "$INSTDIR\Qt5Svg.dll"
        Delete "$INSTDIR\Qt5Widgets.dll"
        Delete "$INSTDIR\select.pyd"
        Delete "$INSTDIR\sip.pyd"
        Delete "$INSTDIR\ucrtbase.dll"
        Delete "$INSTDIR\unicodedata.pyd"
        Delete "$INSTDIR\VCRUNTIME140.dll"
        Delete "$INSTDIR\win32process.pyd"
        Delete "$INSTDIR\_bz2.pyd"
        Delete "$INSTDIR\_ctypes.pyd"
        Delete "$INSTDIR\_hashlib.pyd"
        Delete "$INSTDIR\_lzma.pyd"
        Delete "$INSTDIR\_socket.pyd"
        Delete "$INSTDIR\_ssl.pyd"
        Delete "$INSTDIR\share\icon.png"
        Delete "$INSTDIR\share\version"
        Delete "$INSTDIR\qt5_plugins\iconengines\qsvgicon.dll"
        Delete "$INSTDIR\qt5_plugins\imageformats\qgif.dll"
        Delete "$INSTDIR\qt5_plugins\imageformats\qicns.dll"
        Delete "$INSTDIR\qt5_plugins\imageformats\qico.dll"
        Delete "$INSTDIR\qt5_plugins\imageformats\qjpeg.dll"
        Delete "$INSTDIR\qt5_plugins\imageformats\qsvg.dll"
        Delete "$INSTDIR\qt5_plugins\imageformats\qtga.dll"
        Delete "$INSTDIR\qt5_plugins\imageformats\qtiff.dll"
        Delete "$INSTDIR\qt5_plugins\imageformats\qwbmp.dll"
        Delete "$INSTDIR\qt5_plugins\imageformats\qwebp.dll"
        Delete "$INSTDIR\qt5_plugins\platforms\qminimal.dll"
        Delete "$INSTDIR\qt5_plugins\platforms\qoffscreen.dll"
        Delete "$INSTDIR\qt5_plugins\platforms\qwindows.dll"
        Delete "$INSTDIR\qt5_plugins\printsupport\windowsprintersupport.dll"

        Delete "$INSTDIR\icon.ico"
        Delete "$INSTDIR\uninstall.exe"

        rmDir "$INSTDIR\Include"

        rmDir "$INSTDIR\share"
        rmDir "$INSTDIR\qt5_plugins\iconengines"
        rmDir "$INSTDIR\qt5_plugins\imageformats"
        rmDir "$INSTDIR\qt5_plugins\platforms"
        rmDir "$INSTDIR\qt5_plugins\printsupport"
        rmDir "$INSTDIR\qt5_plugins"
        rmDir "$INSTDIR"

        # remove uninstaller information from the registry
        DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}"
    SectionEnd
!endif
