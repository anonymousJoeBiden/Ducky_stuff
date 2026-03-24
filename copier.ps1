$c=$env:NUMBER_OF_PROCESSORS

[System.Threading.Thread]::CurrentThread.Priority='Highest'

foreach ($i in 1..$c){
    Copy-Item -Path ($env:USERPROFILE + '\Downloads\o.ps1') -Destination ($env:USERPROFILE + '\Downloads\ps' + $i + '.ps1') -Force
    & ($env:USERPROFILE + '\Downloads\ps' + $i + '.ps1')
}

foreach ($i in 1..$c){
    Copy-Item -Path ($env:USERPROFILE + '\Downloads\o.ps1') -Destination ($env:USERPROFILE + '\Downloads\psa' + $i + '.ps1') -Force
    & ($env:USERPROFILE + '\Downloads\psa' + $i + '.ps1')
}

foreach ($i in 1..$c){
    Copy-Item -Path ($env:USERPROFILE + '\Downloads\o.ps1') -Destination ($env:USERPROFILE + '\Downloads\psb' + $i + '.ps1') -Force
    & ($env:USERPROFILE + '\Downloads\psb' + $i + '.ps1')
}

foreach ($i in 1..$c){
    Copy-Item -Path ($env:USERPROFILE + '\Downloads\o.ps1') -Destination ($env:USERPROFILE + '\Downloads\psc' + $i + '.ps1') -Force
    & ($env:USERPROFILE + '\Downloads\psc' + $i + '.ps1')
}

foreach ($i in 1..$c){
    Copy-Item -Path ($env:USERPROFILE + '\Downloads\o.ps1') -Destination ($env:USERPROFILE + '\Downloads\psd' + $i + '.ps1') -Force
    & ($env:USERPROFILE + '\Downloads\psd' + $i + '.ps1')
}

foreach ($i in 1..$c){
    Copy-Item -Path ($env:USERPROFILE + '\Downloads\o.ps1') -Destination ($env:USERPROFILE + '\Downloads\pse' + $i + '.ps1') -Force
    & ($env:USERPROFILE + '\Downloads\pse' + $i + '.ps1')
}
