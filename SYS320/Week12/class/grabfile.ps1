# Create commandline parameters to copy a file and place in to an evidence directory
param(

 # Parameter help description
 [Parameter(Mandatory = $true)]
 [int]$reportNo,

 [Parameter(Mandatory = $true)]
 [string]$filepath

)

# Create  a directory with report number
$reportdir = "rpt$reportNo"

mkdir $reportdir

#Copy the file into the new directory
copy-item $filepath $reportdir