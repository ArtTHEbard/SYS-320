# Get a list of running services

# Get list of Get-Process members
#Get-Process | Get-Member

# Get list of processes, extract name, id , and path.
# Get-Process | Select-Object ProcessName, Id, Path

# Save the Output to a CSV fiel
Get-Process | Select-Object ProcessName, Id, Path | Export-Csv  -Path 'C:\Users\trini\PycharmProjects\SYS-320\Week09\class'
