# Check if antivirus is installed
$antivirus = Get-WmiObject -Class "AntiVirusProduct"

if ($antivirus) {
    Write-Host "Antivirus is installed."
    
    # Check if antivirus is scanning
    $scanStatus = Get-WmiObject -Namespace "root\SecurityCenter2" -Class "AntiVirusProductStatus" | Where-Object {$_.displayName -eq $antivirus.displayName}
    
    if ($scanStatus) {
        Write-Host "Antivirus is scanning."
    } else {
        Write-Host "Antivirus is not scanning."
    }
} else {
    Write-Host "Antivirus is not installed."
}
