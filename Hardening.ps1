# Script : Hardening.ps1
# Purpose: Write a PowerShell script that automates the configuration of the settings: 1.1.5 (L1) and 18.3.2 (L1) from CIS Benchmarks
# Why    : By automating this process it saves a lot of time when running these tasks

# Set "Password must meet complexity requirements"

# Exports the current local security policy settings to a file called secpol.cfg in the root directory of the C: drive
secedit /export /cfg c:\secpol.cfg

# Reads the contents of the 'secpol.cfg' file, replaces the line that specifies the current password complexity
(Get-Content C:\secpol.cfg) -Replace "PasswordComplexity = 0","PasswordComplexity = 1" | Out-File C:\secpol.cfg

# Applies the modified security policy settings from the secpol.cfg file to the local security database (local.sdb) located in the C:\Windows\Security directory
secedit /configure /db c:\windows\security\local.sdb /cfg c:\secpol.cfg /areas SECURITYPOLICY

# Removes the secpol.cfg file that was created, as it is no longer needed.
Remove-Item C:\secpol.cfg -Force

# Disable SMBv1

Set-SmbServerConfiguration -EnableSMB1Protocol $false