# Author: Sam Johnson. 3/31/2022
# Code purpose: Threat Emulation. Code will copy Powershell .exe to the homework folder for Github, and rename it using random variables. 
# The code will also create a Readme file with a ransom message. 

### Task 1
# Copy Powershell to the folder
Copy-Item -Path 'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe' -Destination 'D:\Sec320\SYS-320\Week10\homework\'

# Rename copied file with a random variable.
$ranvar = Get-random -Minimum 1000 -Maximum 1999

$newname = "EnNob-" + $ranvar + '.exe'

Rename-Item -Path 'D:\Sec320\SYS-320\Week10\homework\powershell.exe' -NewName $newname 

# Check to see if file exists. 
$testpath = 'D:\Sec320\SYS-320\Week10\homework\' + $newname
if (Test-Path -Path $testpath) {
    Write-Host -BackgroundColor "green" -ForegroundColor "black" "Good to Go"
} else {
    Write-Host -BackgroundColor "red" -ForegroundColor "black" "NO GO BOSS"
}

### Task 2
# Create a README message with a ransom message. 
$msg = 'If you want your files back, contact me at getpwnd@hacker.net. I look for ward to doing buisness with you, boss.'
$file =  'D:\Sec320\SYS-320\Week10\homework\README;).READ'
$msg | Out-File -FilePath $file

# Check to see if file exists. 
$testpath = 'D:\Sec320\SYS-320\Week10\homework\' + 'README;).READ'
if (Test-Path -Path $testpath) {
    Write-Host -BackgroundColor "green" -ForegroundColor "black" "Good to Go"
} else {
    Write-Host -BackgroundColor "red" -ForegroundColor "black" "NO GO BOSS"
}