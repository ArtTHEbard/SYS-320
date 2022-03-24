# Get a list of running services

# Get list of Get-Process members
#Get-Process | Get-Member

# Get list of processes, extract name, id , and path.
# Get-Process | Select-Object ProcessName, Id, Path

# Output file variable

# Save the Output to a CSV fiel
#Get-Process | Select-Object ProcessName, Id, Path | Export-Csv  -Path 'D:\Sec320\SYS-320\Week09\class\processes.csv'

# $outputname = 'D:\Sec320\SYS-320\Week09\class\services.csv'

# System Services and properties
# Get-Service | get-member
# Get-Service | Select-Object Status, Name, DisplayName, BinaryPathName | Export-Csv -Path $outputname

# Get a list of running services
$outputname = 'D:\Sec320\SYS-320\Week09\class\runningservices.csv'
Get-Service | Where-object { $_.Status -eq "Running" } | Export-Csv $outputname

# Check for output file
if ( Test-Path -Path $outputname) {

    Write-Host -BackgroundColor "Green" -foregroundcolor "white" "Services File was created!"
} else {

    Write-Host -BackgroundColor "Red" -ForegroundColor "white" "Services file wasnt created."
}