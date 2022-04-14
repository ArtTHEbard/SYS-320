# List directory files
# List all files and print full path 
# Get-ChildItem -Recurse -include *.docx, *.pdf, *.txt -Path .\Documents | select FullName

# Get-ChildItem -Recurse -include *.docx, *.pdf, *.txt -Path .\Documents | Export-Csv '.\files.csv'

# import csv file
$filelist = import-csv -Path .\files.csv -header FullName


# Loop results
foreach($f in $filelist){

    Get-ChildItem -path $f.FullName

}