$defender = Get-MpComputerStatus

if ($defender.AntivirusEnabled) {
    Write-Host "Windows Security is installed."
    Start-MpScan -ScanType QuickScan
} else {
    Write-Host "Windows Security is not installed."
}
