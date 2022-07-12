
$program = @'

echo Program is Working >> msg.txt

'@


# Output the "Program" file. 
$program | Out-File -FilePath .\Program.bat