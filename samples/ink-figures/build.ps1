$ErrorActionPreference = 'Stop'
Push-Location $PSScriptRoot
$previousTexInputs = $env:TEXINPUTS
try {
    $templatePath = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../templates'))
    $env:TEXINPUTS = ".;$templatePath;"
    1..2 | ForEach-Object {
        & pdflatex -interaction=nonstopmode -halt-on-error samples.tex
        if ($LASTEXITCODE -ne 0) { throw 'LaTeX compilation failed.' }
    }
    if (Select-String -Path samples.log -Pattern 'Overfull \\hbox|Overfull \\vbox' -Quiet) {
        throw 'Overfull box detected; inspect samples.log.'
    }
    foreach ($name in @('samples.aux','samples.log','samples.out')) {
        if (Test-Path -LiteralPath $name) { Remove-Item -LiteralPath $name }
    }
} finally {
    $env:TEXINPUTS = $previousTexInputs
    Pop-Location
}
