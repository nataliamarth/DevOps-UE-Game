UnrealEditor-Cmd.exe "%CD%\DevOpsGame.uproject" ^
 -nosplash -stdout -Unattended -nopause -nosound -nocontentbrowser -log -ExecCmds="Automation RunTests Project.Functional Tests; Quit" ^
     -TestExit="Automation Test Queue Empty"  ^
    -ReportExportPath="%CD%\Reports" -Log 
