$ErrorActionPreference = "Stop"

$Root = "C:\Codex Projects\YT\SDR Trap"
$SourcePptx = Join-Path $Root "outputs\stop_scaling_chaos_full_deck\Stop_Scaling_Chaos_Codex_Full_Deck.pptx"
$Out = Join-Path $Root "slide_assets_for_clipchamp"
$Temp = Join-Path $Out "temp_powerpoint_fixed"
$Animated = Join-Path $Out "slide_videos_animated_powerpoint"

New-Item -ItemType Directory -Force -Path $Temp, $Animated | Out-Null

function Wait-ForVideo($Presentation, $Label) {
    while ($Presentation.CreateVideoStatus -eq 1) {
        Start-Sleep -Milliseconds 500
    }
    if ($Presentation.CreateVideoStatus -ne 3) {
        throw "PowerPoint video export failed for $Label with status $($Presentation.CreateVideoStatus)"
    }
}

$ppt = New-Object -ComObject PowerPoint.Application
$ppt.Visible = [Microsoft.Office.Core.MsoTriState]::msoTrue
$presentation = $null

try {
    $presentation = $ppt.Presentations.Open($SourcePptx, $false, $false, $false)

    # PowerPoint COM uses points, not inches. 13.333x7.5 inches = 960x540 points.
    $presentation.PageSetup.SlideWidth = 960
    $presentation.PageSetup.SlideHeight = 540

    $slideCount = $presentation.Slides.Count

    $fullRaw = Join-Path $Temp "slides_full_animated_powerpoint_fixed_raw.mp4"
    if (Test-Path $fullRaw) { Remove-Item -LiteralPath $fullRaw -Force }
    $presentation.CreateVideo($fullRaw, $true, 1, 1080, 30, 90)
    Wait-ForVideo $presentation "full deck fixed"

    for ($i = 1; $i -le $slideCount; $i++) {
        $one = $ppt.Presentations.Add([Microsoft.Office.Core.MsoTriState]::msoFalse)
        try {
            $one.PageSetup.SlideWidth = 960
            $one.PageSetup.SlideHeight = 540
            $presentation.Slides.Item($i).Copy()
            $one.Slides.Paste() | Out-Null

            $raw = Join-Path $Temp ("slide_{0:D2}_powerpoint_fixed_raw.mp4" -f $i)
            if (Test-Path $raw) { Remove-Item -LiteralPath $raw -Force }
            $one.CreateVideo($raw, $true, 1, 1080, 30, 90)
            Wait-ForVideo $one ("slide $i fixed")
        }
        finally {
            if ($one -ne $null) { $one.Close() }
        }
    }
}
finally {
    if ($presentation -ne $null) { $presentation.Close() }
    $ppt.Quit()
}

Write-Output "Fixed PowerPoint animated export complete."
