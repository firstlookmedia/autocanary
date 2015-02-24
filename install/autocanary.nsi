!define APPNAME "AutoCanary"
!define BINPATH "..\dist"

# change these with each release
!define INSTALLSIZE 12292
!define VERSIONMAJOR 0
!define VERSIONMINOR 1
!define VERSIONSTRING "0.1"

RequestExecutionLevel admin

Name "AutoCanary"
InstallDir "$PROGRAMFILES\${APPNAME}"
LicenseData "license.txt"
Icon "icon.ico"

!include LogicLib.nsh

Page license
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
    !system "signtool.exe sign /v /d $\"Uninstall AutoCanary$\" /a /tr http://www.startssl.com/timestamp $%TEMP%\uninstall.exe" = 0
    
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
    File "${BINPATH}\autocanary.exe"
    File "${BINPATH}\library.zip"
	File "${BINPATH}\w9xpopen.exe"

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
        Delete "$INSTDIR\autocanary.exe"
        Delete "$INSTDIR\library.zip"
		Delete "$INSTDIR\w9xpopen.exe"
        Delete "$INSTDIR\icon.ico"
        Delete "$INSTDIR\uninstall.exe"
        rmDir "$INSTDIR"

        # remove uninstaller information from the registry
        DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}"
    SectionEnd
!endif
