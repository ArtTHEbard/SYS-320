cls
# Login to a remote SSH server
# New-SSHSession -ComputerName '172.31.56.50' -Credential (Get-Credential kali)

<#
while ($True) {

    # Add a prompt top run commands
    $the_cmd = read-host -Prompt "Please Enter a command: "

    # Run Command on remote SSH server
    (Invoke-SSHCommand -index 3 $the_cmd).Output

}
#>

Set-SCPItem -ComputerName '172.31.56.50' -Credential (Get-Credential kali) -Path 'D:\Sec320\SYS-320\Week11\class\test.txt' -Destination '/home/kali/'
