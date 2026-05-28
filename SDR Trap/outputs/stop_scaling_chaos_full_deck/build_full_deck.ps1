$ErrorActionPreference = 'Stop'

$outDir = 'C:\Codex Projects\YT\SDR Trap\outputs\stop_scaling_chaos_full_deck'
$assetDir = Join-Path $outDir 'assets'
$pptxPath = Join-Path $outDir 'Stop_Scaling_Chaos_Codex_Full_Deck.pptx'

function RgbFromHex($hex) {
  return [Convert]::ToInt32($hex.Substring(4,2) + $hex.Substring(2,2) + $hex.Substring(0,2), 16)
}

$slides = @(
  @{ts='0:00-0:07'; heading=@(@{t='Founder raises ';c='FFFFFF'},@{t='funding';c='E7FF00'},@{t='.';c='FFFFFF'}); support=''; caption='What could go wrong?'; cue='A founder raises another round of funding.'},
  @{ts='0:07-0:18'; heading=@(@{t='First move: ';c='FFFFFF'},@{t='hire SDRs';c='E7FF00'},@{t='.';c='FFFFFF'}); support=''; caption='The outbound cinematic universe begins.'; cue='Their first move? Hire two SDRs and a VP of Sales...'},
  @{ts='0:18-0:27'; heading=@(@{t='3 months ';c='FFFFFF'},@{t='later';c='E7FF00'},@{t='...';c='FFFFFF'}); support='Calendar: empty.'; caption='Pipeline looking spacious.'; cue='Three months later, their calendar is emptier than...'},
  @{ts='0:27-0:36'; heading=@(@{t='Burn rate: ';c='FFFFFF'},@{t='vertical';c='FF3333'},@{t='.';c='FFFFFF'}); support=''; caption='At least something is growing.'; cue='Their burn rate is vertical.'},
  @{ts='0:36-0:45'; heading=@(@{t='You aren''t ';c='FFFFFF'},@{t='scaling';c='E7FF00'},@{t='.';c='FFFFFF'}); support='You''re gambling.'; caption='The house always wins.'; cue='You are not scaling. You are gambling.'},
  @{ts='0:45-0:55'; heading=@(@{t='You copied the ';c='FFFFFF'},@{t='payroll';c='E7FF00'},@{t='.';c='FFFFFF'}); support='Not the process.'; caption='Org chart != go-to-market strategy.'; cue='You copied the payroll, not the process.'},
  @{ts='0:55-1:05'; heading=@(@{t='The public version ';c='FFFFFF'},@{t='looks easy';c='E7FF00'},@{t='.';c='FFFFFF'}); support=''; caption='The backstory was not sponsored.'; cue='The public version looks easy.'},
  @{ts='1:05-1:17'; heading=@(@{t='You don''t see the ';c='FFFFFF'},@{t='pain';c='FF3333'},@{t='.';c='FFFFFF'}); support=''; caption='This is where the playbook was born.'; cue='You do not see the pain behind the playbook.'},
  @{ts='1:17-1:30'; heading=@(@{t='No playbook. ';c='FFFFFF'},@{t='Just vibes';c='E7FF00'},@{t='.';c='FFFFFF'}); support=''; caption='Good luck, Chad.'; cue='Without a playbook, the SDR is walking into the unknown.'},
  @{ts='1:30-1:41'; heading=@(@{t='A sequence is ';c='FFFFFF'},@{t='not a playbook';c='E7FF00'},@{t='.';c='FFFFFF'}); support=''; caption='Downloaded. Not validated.'; cue='A cold email sequence is not a real outbound playbook.'},
  @{ts='1:41-1:56'; heading=@(@{t='Message-market ';c='FFFFFF'},@{t='fit';c='E7FF00'},@{t='.';c='FFFFFF'}); support=''; caption='Dark science, but with spreadsheets.'; cue='The real thing you are building is message-market fit.'},
  @{ts='1:56-2:15'; heading=@(@{t='Don''t be ';c='FFFFFF'},@{t='creepy';c='FF3333'},@{t='.';c='FFFFFF'}); support=''; caption='Personalization has a limit.'; cue='Personalization has a limit.'},
  @{ts='2:15-2:28'; heading=@(@{t='Founders research ';c='FFFFFF'},@{t='everything';c='E7FF00'},@{t='.';c='FFFFFF'}); support=''; caption='Before buying one $49 tool.'; cue='Founders research everything before buying.'},
  @{ts='2:28-2:43'; heading=@(@{t='But when ';c='FFFFFF'},@{t='selling';c='E7FF00'},@{t='...';c='FFFFFF'}); support='That is called delulu.'; caption='Bold strategy.'; cue='But when selling, they expect one cold email to do all the work.'},
  @{ts='3:00-3:12'; heading=@(@{t='SDRs are not the ';c='FFFFFF'},@{t='machine';c='E7FF00'},@{t='.';c='FFFFFF'}); support=''; caption='Operator != engine.'; cue='SDRs are not the machine.'},
  @{ts='3:12-3:27'; heading=@(@{t='The playbook is the ';c='FFFFFF'},@{t='machine';c='4CFF6A'},@{t='.';c='FFFFFF'}); support=''; caption='Build this first.'; cue='The playbook is the machine.'},
  @{ts='3:27-3:45'; heading=@(@{t='Broken process + more people = ';c='FFFFFF'},@{t='bigger mess';c='FF3333'},@{t='.';c='FFFFFF'}); support=''; caption='Congrats, you scaled chaos.'; cue='Broken process plus more people equals a bigger mess.'},
  @{ts='3:45-3:57'; heading=@(@{t='Just send ';c='FFFFFF'},@{t='10,000 more emails';c='FF3333'},@{t='.';c='FFFFFF'}); support=''; caption='Every weak strategy''s favorite button.'; cue='The default answer becomes more volume.'},
  @{ts='3:57-4:13'; heading=@(@{t='Dead message. ';c='FFFFFF'},@{t='Faster rejection';c='FF3333'},@{t='.';c='FFFFFF'}); support=''; caption='Industrialized rejection.'; cue='A dead message just creates faster rejection.'},
  @{ts='4:13-4:32'; heading=@(@{t='2 people ';c='E7FF00'},@{t='out of 100.';c='FFFFFF'}); support=''; caption='That''s the game.'; cue='Maybe two people out of a hundred say yes.'},
  @{ts='4:32-4:55'; heading=@(@{t='Find why they said ';c='FFFFFF'},@{t='yes';c='4CFF6A'},@{t='.';c='FFFFFF'}); support=''; caption='Pain? Timing? Competitor annoyed them?'; cue='The job is to find why those two said yes.'},
  @{ts='5:00-5:18'; heading=@(@{t='The first 6 months are ';c='FFFFFF'},@{t='not wasted';c='E7FF00'},@{t='.';c='FFFFFF'}); support=''; caption='Distribution compounds silently.'; cue='The first six months are not wasted if you are building the system.'},
  @{ts='5:18-5:32'; heading=@(@{t='Not the SDR. Not the agency. ';c='FFFFFF'},@{t='Not the tool';c='FF3333'},@{t='.';c='FFFFFF'}); support='The machine.'; caption='The real asset.'; cue='The real asset is not the SDR, agency, or tool. It is the machine.'},
  @{ts='5:32-5:46'; heading=@(@{t='Build the ';c='FFFFFF'},@{t='playbook';c='4CFF6A'},@{t=' first.';c='FFFFFF'}); support=''; caption='Then scale.'; cue='Build the playbook first. Then scale.'}
)

$pp = $null
try {
  $pp = New-Object -ComObject PowerPoint.Application
  $pres = $pp.Presentations.Add()
  $pres.PageSetup.SlideWidth = 960
  $pres.PageSetup.SlideHeight = 540

  for ($i = 0; $i -lt $slides.Count; $i++) {
    $item = $slides[$i]
    $slide = $pres.Slides.Add($i + 1, 12)
    $imgPath = Join-Path $assetDir ("slide{0:D2}.png" -f ($i + 1))

    $slide.FollowMasterBackground = $false
    $slide.Background.Fill.ForeColor.RGB = 0

    # Center the image lower than the headline so the text does not hide the image's top margin.
    $pic = $slide.Shapes.AddPicture($imgPath, $false, $true, 72, 96, 816, 459)
    $pic.ZOrder(1)

    $top = $slide.Shapes.AddShape(1, 0, 0, 960, 104)
    $top.Fill.ForeColor.RGB = 0
    $top.Fill.Transparency = 0.03
    $top.Line.Visible = 0

    $bottom = $slide.Shapes.AddShape(1, 0, 448, 960, 92)
    $bottom.Fill.ForeColor.RGB = 0
    $bottom.Fill.Transparency = 0.08
    $bottom.Line.Visible = 0

    $heading = $slide.Shapes.AddTextbox(1, 30, 24, 900, 62)
    $heading.TextFrame.MarginLeft = 0
    $heading.TextFrame.MarginRight = 0
    $heading.TextFrame.MarginTop = 0
    $heading.TextFrame.MarginBottom = 0
    $heading.TextFrame.WordWrap = $false
    $heading.TextFrame.AutoSize = 1
    $headingText = ''
    foreach ($part in $item.heading) { $headingText += $part.t }
    $heading.TextFrame.TextRange.Text = $headingText
    $heading.TextFrame.TextRange.Font.Name = 'Arial'
    $heading.TextFrame.TextRange.Font.Bold = $true
    $heading.TextFrame.TextRange.Font.Size = 42
    $heading.TextFrame.TextRange.Font.Color.RGB = 16777215
    $pos = 1
    foreach ($part in $item.heading) {
      $len = $part.t.Length
      $range = $heading.TextFrame.TextRange.Characters($pos, $len)
      $range.Font.Color.RGB = RgbFromHex $part.c
      $pos += $len
    }
    if ($headingText.Length -gt 36) { $heading.TextFrame.TextRange.Font.Size = 36 }
    if ($headingText.Length -gt 48) { $heading.TextFrame.TextRange.Font.Size = 31 }

    if ($item.support -ne '') {
      $support = $slide.Shapes.AddTextbox(1, 40, 405, 880, 36)
      $support.TextFrame.MarginLeft = 0
      $support.TextFrame.MarginRight = 0
      $support.TextFrame.MarginTop = 0
      $support.TextFrame.MarginBottom = 0
      $support.TextFrame.TextRange.Text = $item.support
      $support.TextFrame.TextRange.Font.Name = 'Arial'
      $support.TextFrame.TextRange.Font.Bold = $true
      $support.TextFrame.TextRange.Font.Size = 25
      $support.TextFrame.TextRange.Font.Color.RGB = 16777215
      $support.TextFrame.TextRange.ParagraphFormat.Alignment = 2
      $null = $slide.TimeLine.MainSequence.AddEffect($support, 10, 0, 1)
    }

    $caption = $slide.Shapes.AddTextbox(1, 40, 476, 880, 38)
    $caption.TextFrame.MarginLeft = 0
    $caption.TextFrame.MarginRight = 0
    $caption.TextFrame.MarginTop = 0
    $caption.TextFrame.MarginBottom = 0
    $caption.TextFrame.TextRange.Text = $item.caption
    $caption.TextFrame.TextRange.Font.Name = 'Arial'
    $caption.TextFrame.TextRange.Font.Bold = $true
    $caption.TextFrame.TextRange.Font.Size = 23
    $caption.TextFrame.TextRange.Font.Color.RGB = RgbFromHex 'E7FF00'
    if ($item.caption.Length -gt 34) { $caption.TextFrame.TextRange.Font.Size = 20 }
    $caption.TextFrame.TextRange.ParagraphFormat.Alignment = 2

    $notes = $slide.NotesPage.Shapes.Placeholders(2)
    $notes.TextFrame.TextRange.Text = "Timestamp: $($item.ts)`r`nNarration cue: $($item.cue)`r`nAnimation cue: Reveal visual first, then heading/highlight, then support text if present, then caption."

    $null = $slide.TimeLine.MainSequence.AddEffect($pic, 10, 0, 1)
    $null = $slide.TimeLine.MainSequence.AddEffect($heading, 10, 0, 1)
    $null = $slide.TimeLine.MainSequence.AddEffect($caption, 10, 0, 1)
  }

  if (Test-Path $pptxPath) { Remove-Item -LiteralPath $pptxPath -Force }
  $pres.SaveAs($pptxPath)
  $pres.Close()
  Write-Output $pptxPath
}
finally {
  if ($pp) { $pp.Quit() | Out-Null }
}
