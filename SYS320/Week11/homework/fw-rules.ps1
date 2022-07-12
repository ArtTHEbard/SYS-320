# Array of websites containing threat intell
$drop_urls = @('https://rules.emergingthreats.net/blockrules/emerging-botcc.rules','https://rules.emergingthreats.net/blockrules/compromised-ips.txt')

# Loop through the URLs for the rules list
foreach ($u in $drop_urls){
    
    # Extract the Filename
    $temp = $u.Split("/")
    
    #$temp[0]
    #$temp[2]

    # The last em=lemetn in the array plucked off is the filename
    $file_name = $temp[-1]
    # Check for file
    $file_path = 'D:\Sec320\SYS-320\Week11\homework\' + $file_name
    if (Test-Path -Path $file_path){
        continue 
    } else {
    
        # Download th rules list
    
    Invoke-WebRequest -Uri $u -OutFile $file_path
    }
}

# Array containting the filename
$input_paths = @('Week11\homework\compromised-ips.txt', 'Week11\homework\emerging-botcc.rules')

#Extract the IP addresses
$regex_drop = '\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

# Append the IP addresses to the temp IP list. 
select-string -path $input_paths -pattern $regex_drop |
Foreach-object { $_.Matches } | 
foreach-object { $_.Value } | Sort-Object | Get-Unique |
Out-File -FilePath "Week11\homework\ips-bad.tmp"

$var = Read-host -Prompt "Please enter Windows or IPTables"

switch ($var)
{
    Windows
    {
        # Get the IP addresses discovered, loop through and replace the beginnign of the line with the Windows netsh systax
        # Run a small script to cycel through Rule names. 
        (Get-Content -Path ".\Week11\homework\ips-bad.tmp") | 
        Foreach-object { $_ -replace "^","netsh advfirewall firewall add rule name='SYS320' dir=in action=block remoteip=" -replace "$"} |
        Out-File -FilePath "Week11\homework\windows.ps1"
    }
    IPTables
    {
        # Get the IP addresses discovered, loop through and replace the beginnign of the line with the IPTables systax
        # After the IP address, add the remaining IPTables systax and save the results to a file. 
        # iptables -A INPUT -s 108.191.2.72 -j DROP
        (Get-Content -Path ".\Week11\homework\ips-bad.tmp") | 
        Foreach-object { $_ -replace "^","iptables -A INPUT -s " -replace "$", " -j DROP" } |
        Out-File -FilePath "Week11\homework\iptables.bash"
        Set-SCPItem -ComputerName '172.31.56.50' -Credential (Get-Credential kali) -Path '.\Week11\homework\iptables.bash' -Destination '/home/kali/'
    }
}
