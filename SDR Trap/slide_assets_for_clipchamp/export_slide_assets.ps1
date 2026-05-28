$ErrorActionPreference = "Stop"

$Root = "C:\Codex Projects\YT\SDR Trap"
$SourcePptx = Join-Path $Root "outputs\stop_scaling_chaos_full_deck\Stop_Scaling_Chaos_Codex_Full_Deck.pptx"
$Out = Join-Path $Root "slide_assets_for_clipchamp"
$SlideVideos = Join-Path $Out "slide_videos"
$SlideImages = Join-Path $Out "slide_images"
$Temp = Join-Path $Out "temp"

New-Item -ItemType Directory -Force -Path $Out, $SlideVideos, $SlideImages, $Temp | Out-Null

function Wait-ForVideo($Presentation, $Label) {
    $last = -1
    while ($Presentation.CreateVideoStatus -eq 1) {
        Start-Sleep -Seconds 2
        if ($Presentation.CreateVideoStatus -ne $last) {
            $last = $Presentation.CreateVideoStatus
        }
    }
    if ($Presentation.CreateVideoStatus -ne 3) {
        throw "PowerPoint video export failed for $Label with status $($Presentation.CreateVideoStatus)"
    }
}

$ppSaveAsOpenXMLPresentation = 24
$ppLayoutBlank = 12

$ppt = New-Object -ComObject PowerPoint.Application
$ppt.Visible = [Microsoft.Office.Core.MsoTriState]::msoTrue
$presentation = $null

try {
    $presentation = $ppt.Presentations.Open($SourcePptx, $false, $false, $false)
    $presentation.PageSetup.SlideWidth = 13.333333
    $presentation.PageSetup.SlideHeight = 7.5
    $slideCount = $presentation.Slides.Count

    for ($i = 1; $i -le $slideCount; $i++) {
        $img = Join-Path $SlideImages ("slide_{0:D2}.png" -f $i)
        $presentation.Slides.Item($i).Export($img, "PNG", 1920, 1080)
    }

    $fullRaw = Join-Path $Temp "slides_full_animated_powerpoint_raw.mp4"
    if (Test-Path $fullRaw) { Remove-Item -LiteralPath $fullRaw -Force }
    $presentation.CreateVideo($fullRaw, $true, 1, 1080, 30, 85)
    Wait-ForVideo $presentation "full deck"

    for ($i = 1; $i -le $slideCount; $i++) {
        $one = $ppt.Presentations.Add([Microsoft.Office.Core.MsoTriState]::msoFalse)
        try {
            $presentation.Slides.Item($i).Copy()
            $one.Slides.Paste() | Out-Null
            if ($one.Slides.Count -gt 1) {
                for ($d = $one.Slides.Count; $d -ge 2; $d--) {
                    $one.Slides.Item($d).Delete()
                }
            }
            $one.PageSetup.SlideWidth = 13.333333
            $one.PageSetup.SlideHeight = 7.5
            $raw = Join-Path $Temp ("slide_{0:D2}_powerpoint_raw.mp4" -f $i)
            if (Test-Path $raw) { Remove-Item -LiteralPath $raw -Force }
            $one.CreateVideo($raw, $true, 1, 1080, 30, 85)
            Wait-ForVideo $one ("slide $i")
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

Write-Output "PowerPoint raw export complete."
