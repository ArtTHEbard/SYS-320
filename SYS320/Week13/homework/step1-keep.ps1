# Author: Sam Johnson. 3/31/2022
# Code purpose: Threat Emulation. Code will copy Powershell .exe to the homework folder for Github, and rename it using random variables. 
# The code will also create a Readme file with a ransom message. 

### Task 1
# Copy Powershell to the folder
Copy-Item -Path 'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe' -Destination 'D:\Sec320\SYS-320\Week13\homework\'

# Rename copied file with a random variable.
$ranvar = Get-random -Minimum 1000 -Maximum 1999

$newname = "EnNob-" + $ranvar + '.exe'

Rename-Item -Path 'D:\Sec320\SYS-320\Week13\homework\powershell.exe' -NewName $newname 

# Check to see if file exists. 
$testpath = 'D:\Sec320\SYS-320\Week13\homework\' + $newname
if (Test-Path -Path $testpath) {
    Write-Host -BackgroundColor "green" -ForegroundColor "black" "Good to Go"
} else {
    Write-Host -BackgroundColor "red" -ForegroundColor "black" "NO GO BOSS"
}

### Task 2
# Create a README message with a ransom message. 
$msg = 'If you want your files back, contact me at getpwnd@hacker.net. I look forward to doing buisness with you, boss.'
$file =  'D:\Sec320\SYS-320\Week13\homework\README;).READ'
$msg | Out-File -FilePath $file

# Check to see if file exists. 
$testpath = 'D:\Sec320\SYS-320\Week13\homework\' + 'README;).READ'
if (Test-Path -Path $testpath) {
    Write-Host -BackgroundColor "green" -ForegroundColor "black" "Good to Go"
} else {
    Write-Host -BackgroundColor "red" -ForegroundColor "black" "NO GO BOSS"
}

# I do not feel confortable running this or other commands in Task 2 on my local machine. CFA is a Windows security function that inspects executable files that have the ability to make changes to sesitive computer files that the user can specify. 
# This affects PYSA's ability to encrypt sensitive or critical files, as the CFA function can catch the malware in the act and prevent it from fulfilling its tasks. 
# Write-Host "Set-MpPreference -EnableControlledFolderAccess Disabled"

$outputbat = @'
del .\Week13\homework\step1.ps1
del .\Week13\homework\step2.ps1
rmdir /s D:\Sec320\SYS-320\Week13\homework\extract
del .\Week13\homework\extract.zip
del .\Week13\homework\targets.csv
'@

$outputbat | Out-File -FilePath .\Week13\homework\update.bat