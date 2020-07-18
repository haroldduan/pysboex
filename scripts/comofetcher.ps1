<#
**** Comofetcher,means [COM Object Fetcher]'s abbreviation.
**** Programmer:Harold.Duan
**** Date:20200629
**** Reason: COM object fetcher running scripts.
#>
# gwmi -list | ?{ $_.Name -cmatch "COM" }

function Get-ProgID {
    #.Synopsis
    #   Gets all of the ProgIDs registered on a system
    #.Description
    #   Gets all ProgIDs registered on the system.  The ProgIDs returned can be used with New-Object -comObject
    #.Example
    #   Get-ProgID
    #.Example
    #   Get-ProgID | Where-Object { $_.ProgID -like "*Image*" } 
    param()
    $paths = @("REGISTRY::HKEY_CLASSES_ROOT\CLSID")
    if ($env:Processor_Architecture -eq "amd64") {
        $paths+="REGISTRY::HKEY_CLASSES_ROOT\Wow6432Node\CLSID"
    }
    Get-ChildItem $paths -include VersionIndependentPROGID -recurse |
    Select-Object @{
        Name='ProgID'
        Expression={$_.GetValue("")}
    }, @{
        Name='OSBit'
        Expression={
            if ($env:Processor_Architecture -eq "amd64") {
                # $_.PSPath.Contains("Wow6432Node")
                if($_.PSPath.Contains("Wow6432Node")){ "x64" } else { "x86" }
            } else {
                # $true
                "x86"
            }
        }
    }
}

# Get-ProgID

Write-Output 'Welcome to Comofetcher!'
$os_bit = Read-Host 'Choose os bit,
0.all(default)
1.x64
2.x86
'
switch($os_bit){
    "0" {$os_bit = "all";break;}
    "1" {$os_bit = "x64";break;}
    "2" {$os_bit = "x86";break;}
    Default {$os_bit = "all";break;}
}
# Write-Output $os_bit
Write-Output "You choosed: [$os_bit]!"

$key_words = Read-Host 'You can set some key words for fetching the COM Objects...'
Write-Output "Your key words: [$key_words]!"

Write-Output "Fetching..."

#Get-ProgID | Where-Object { ((if($os_bit -ne "all"){ $_.OSBit -eq $os_bit }) -and (if ($key_words -ne "") { $_.ProgID -like "*$key_words*" }))}

if ($os_bit -eq "all") {
    if ($key_words -eq "") {
        Get-ProgID   
    }
    else {
        Get-ProgID | Where-Object { $_.ProgID -like "*$key_words*" }
    }
}
else {
    if ($key_words -eq "") {
        Get-ProgID | Where-Object { $_.OSBit -eq $os_bit }
    } else {
        Write-Output "*$key_words*"
        Get-ProgID | Where-Object { ($_.OSBit -eq $os_bit) -and ($_.ProgID -like "*$key_words*") }
    }
}

Write-Output "Done!"