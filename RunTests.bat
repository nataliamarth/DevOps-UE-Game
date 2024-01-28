"C:\Program Files\Epic Games\UE_5.0\Engine\Binaries\Win64\UnrealEditor-Cmd.exe" "%CD%\DevOpsGame.uproject" ^
 -nosplash -stdout -Unattended -nopause -nosound -nocontentbrowser -log -ExecCmds="Automation RunTests Project.Functional Tests; Quit" ^
     -TestExit="Automation Test Queue Empty"  ^
    -ReportExportPath="%CD%\Reports" -Log 
