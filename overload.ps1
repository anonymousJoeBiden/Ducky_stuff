$c=$env:NUMBER_OF_PROCESSORS

[System.Threading.Thread]::CurrentThread.Priority='Highest'

foreach ($i in 1..$c){
    Start-Job -ScriptBlock{
        # $r=1
        # foreach($j in 1..0x7FFFFFFF){
        #     $r=$r*$j
        # }
        while ($true) {
            $null = [Math]::Sqrt(1234567891011)
        }
    }
}
