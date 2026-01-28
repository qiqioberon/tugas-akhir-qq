param(
    [string]$inputFile = "TugasAkhirMuhammadAqilFarrukh.docx",
    [string]$outputFile = ""
)

if ($outputFile -eq "") {
    $baseName = [System.IO.Path]::GetFileNameWithoutExtension($inputFile)
    $outputFile = "$baseName.md"
}

pandoc $inputFile -t markdown -o $outputFile

Write-Host "✅ Konversi selesai: $outputFile"
