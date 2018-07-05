Get-ChildItem "C:\Github\WebSemantica_2018_1\portal_transparencia\extrator\working_area" |
Foreach-Object {
	Get-Content .\$_ | Set-Content -Encoding utf8 $_
}

$files = Get-ChildItem "C:\Github\WebSemantica_2018_1\portal_transparencia\extrator\working_area"

foreach($file in $files)
{
    $content = Get-Content $file.FullName
    $content | Out-File $file.FullName -Encoding $Utf8NoBomEncoding
}

$files = Get-ChildItem "C:\Github\WebSemantica_2018_1\portal_transparencia\extrator\working_area"

foreach($file in $files)
{
    $content = Get-Content $file.FullName
    $Utf8NoBomEncoding = New-Object System.Text.UTF8Encoding $False
    $content | Out-File $file.FullName -Encoding utf8
}


$utf8 = New-Object System.Text.UTF8Encoding $false