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
