from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import shutil
import xml.etree.ElementTree as ET

SRC = Path(r"C:\Codex Projects\YT\SDR Trap\Stop_Scaling_Chaos.pptx")
OUT_DIR = Path(r"C:\Codex Projects\YT\SDR Trap\outputs\stop_scaling_chaos_3_slide_test")
OUT = OUT_DIR / "Stop_Scaling_Chaos_Codex_3_Slide_Test.pptx"
ASSETS = OUT_DIR / "assets"

P_NS = "http://schemas.openxmlformats.org/presentationml/2006/main"
A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"

EMU_W = 12192000
EMU_H = 6858000

SLIDES = [
    {
        "image": "slide1_founder.png",
        "title": [("Founder raises ", "FFFFFF"), ("funding", "E7FF00"), (".", "FFFFFF")],
        "title_size": 5500,
        "caption": "What could go wrong?",
        "caption_y": 6050000,
        "extra": [("SERIES A", 4370000, 4320000, 3600000, 560000, 3000, "E7FF00")],
        "note": "Timestamp: 0:00-0:07\nNarration cue: A founder raises another round of funding.\nAnimation cue: Reveal image, then headline, then caption.",
    },
    {
        "image": "slide2_team.png",
        "title": [("First move: ", "FFFFFF"), ("hire SDRs", "E7FF00"), (".", "FFFFFF")],
        "title_size": 5200,
        "caption": "The outbound cinematic universe begins.",
        "caption_y": 6070000,
        "extra": [],
        "note": "Timestamp: 0:07-0:18\nNarration cue: Their first move? Hire two SDRs and a VP of Sales...\nAnimation cue: Reveal SDRs, then VP Sales, then caption.",
    },
    {
        "image": "slide3_calendar.png",
        "title": [("3 months ", "FFFFFF"), ("later", "E7FF00"), ("...", "FFFFFF")],
        "title_size": 5800,
        "caption": "Pipeline looking spacious.",
        "caption_y": 6050000,
        "extra": [("Calendar: empty.", 502000, 5410000, 11100000, 450000, 2600, "FFFFFF")],
        "note": "Timestamp: 0:18-0:27\nNarration cue: Three months later, their calendar is emptier than...\nAnimation cue: Reveal calendar, then headline, then Calendar: empty, then caption.",
    },
]


def esc(text):
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def tx_body_rich(parts, font_size, align="l"):
    runs = []
    for text, color in parts:
        runs.append(
            f"""
            <a:r>
              <a:rPr lang="en-US" sz="{font_size}" b="1" dirty="0">
                <a:solidFill><a:srgbClr val="{color}"/></a:solidFill>
                <a:latin typeface="Arial"/>
              </a:rPr>
              <a:t>{esc(text)}</a:t>
            </a:r>"""
        )
    return f"""
      <p:txBody>
        <a:bodyPr wrap="none" anchor="mid"><a:spAutoFit/></a:bodyPr>
        <a:lstStyle/>
        <a:p>
          <a:pPr algn="{align}"/>
          {''.join(runs)}
          <a:endParaRPr lang="en-US" sz="{font_size}" b="1">
            <a:latin typeface="Arial"/>
          </a:endParaRPr>
        </a:p>
      </p:txBody>"""


def tx_body_plain(text, font_size, color, align="ctr"):
    return f"""
      <p:txBody>
        <a:bodyPr wrap="none" anchor="mid"><a:spAutoFit/></a:bodyPr>
        <a:lstStyle/>
        <a:p>
          <a:pPr algn="{align}"/>
          <a:r>
            <a:rPr lang="en-US" sz="{font_size}" b="1" dirty="0">
              <a:solidFill><a:srgbClr val="{color}"/></a:solidFill>
              <a:latin typeface="Arial"/>
            </a:rPr>
            <a:t>{esc(text)}</a:t>
          </a:r>
          <a:endParaRPr lang="en-US" sz="{font_size}" b="1">
            <a:latin typeface="Arial"/>
          </a:endParaRPr>
        </a:p>
      </p:txBody>"""


def text_shape(shape_id, name, x, y, w, h, tx_body):
    return f"""
    <p:sp>
      <p:nvSpPr>
        <p:cNvPr id="{shape_id}" name="{name}"/>
        <p:cNvSpPr txBox="1"/>
        <p:nvPr/>
      </p:nvSpPr>
      <p:spPr>
        <a:xfrm><a:off x="{x}" y="{y}"/><a:ext cx="{w}" cy="{h}"/></a:xfrm>
        <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
        <a:noFill/><a:ln><a:noFill/></a:ln>
      </p:spPr>
      {tx_body}
    </p:sp>"""


def overlay_rect(shape_id, y, h, transparency):
    return f"""
    <p:sp>
      <p:nvSpPr><p:cNvPr id="{shape_id}" name="Dark overlay"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
      <p:spPr>
        <a:xfrm><a:off x="0" y="{y}"/><a:ext cx="{EMU_W}" cy="{h}"/></a:xfrm>
        <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
        <a:solidFill><a:srgbClr val="000000"><a:alpha val="{transparency}"/></a:srgbClr></a:solidFill>
        <a:ln><a:noFill/></a:ln>
      </p:spPr>
    </p:sp>"""


def slide_xml(item, idx):
    sp_id = 10
    shapes = [
        f"""
    <p:pic>
      <p:nvPicPr>
        <p:cNvPr id="4" name="Generated visual {idx}"/>
        <p:cNvPicPr><a:picLocks noChangeAspect="1"/></p:cNvPicPr>
        <p:nvPr/>
      </p:nvPicPr>
      <p:blipFill>
        <a:blip r:embed="rId2"/>
        <a:stretch><a:fillRect/></a:stretch>
      </p:blipFill>
      <p:spPr>
        <a:xfrm><a:off x="0" y="0"/><a:ext cx="{EMU_W}" cy="{EMU_H}"/></a:xfrm>
        <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
      </p:spPr>
    </p:pic>""",
        overlay_rect(5, 0, 1450000, 22000),
        overlay_rect(6, 5800000, 1050000, 16000),
        text_shape(sp_id, "Editable headline", 380000, 295000, 11480000, 850000, tx_body_rich(item["title"], item["title_size"])),
    ]
    sp_id += 1
    for text, x, y, w, h, size, color in item["extra"]:
        shapes.append(text_shape(sp_id, "Editable support text", x, y, w, h, tx_body_plain(text, size, color)))
        sp_id += 1
    shapes.append(text_shape(sp_id, "Editable caption", 502000, item["caption_y"], 11100000, 500000, tx_body_plain(item["caption"], 2600, "E7FF00")))
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="{A_NS}" xmlns:r="{R_NS}" xmlns:p="{P_NS}">
  <p:cSld>
    <p:bg><p:bgPr><a:solidFill><a:srgbClr val="030303"/></a:solidFill><a:effectLst/></p:bgPr></p:bg>
    <p:spTree>
      <p:nvGrpSpPr>
        <p:cNvPr id="1" name=""/>
        <p:cNvGrpSpPr/>
        <p:nvPr/>
      </p:nvGrpSpPr>
      <p:grpSpPr>
        <a:xfrm>
          <a:off x="0" y="0"/><a:ext cx="0" cy="0"/>
          <a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/>
        </a:xfrm>
      </p:grpSpPr>
      {''.join(shapes)}
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sld>"""


def rels_xml(idx):
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="{REL_NS}">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="../media/codex_slide{idx}.png"/>
</Relationships>"""


def trim_presentation(xml_bytes):
    root = ET.fromstring(xml_bytes)
    ns = {"p": P_NS, "r": R_NS}
    sld_list = root.find("p:sldIdLst", ns)
    for child in list(sld_list):
        sld_list.remove(child)
    for i in range(1, 4):
        sld = ET.SubElement(sld_list, f"{{{P_NS}}}sldId")
        sld.set("id", str(255 + i))
        sld.set(f"{{{R_NS}}}id", f"rId{100 + i}")
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def trim_pres_rels(xml_bytes):
    root = ET.fromstring(xml_bytes)
    keep = []
    for el in root:
        typ = el.attrib.get("Type", "")
        target = el.attrib.get("Target", "")
        if typ.endswith("/slide"):
            n = int(Path(target).stem.replace("slide", ""))
            if n <= 3:
                el.set("Id", f"rId{100 + n}")
                keep.append(el)
        elif typ.endswith("/slideMaster") or typ.endswith("/theme") or typ.endswith("/presProps") or typ.endswith("/viewProps") or typ.endswith("/tableStyles"):
            keep.append(el)
    root[:] = keep
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def main():
    replacements = {
        "ppt/presentation.xml": lambda data: trim_presentation(data),
        "ppt/_rels/presentation.xml.rels": lambda data: trim_pres_rels(data),
    }
    with ZipFile(SRC, "r") as zin, ZipFile(OUT, "w", ZIP_DEFLATED) as zout:
        names = set(zin.namelist())
        for name in zin.namelist():
            if name in [f"ppt/slides/slide{i}.xml" for i in range(1, 4)]:
                zout.writestr(name, slide_xml(SLIDES[int(name[-5]) - 1], int(name[-5])))
            elif name in [f"ppt/slides/_rels/slide{i}.xml.rels" for i in range(1, 4)]:
                zout.writestr(name, rels_xml(int(name[-10])))
            elif name in replacements:
                zout.writestr(name, replacements[name](zin.read(name)))
            else:
                zout.writestr(name, zin.read(name))
        for idx, item in enumerate(SLIDES, 1):
            zout.write(ASSETS / item["image"], f"ppt/media/codex_slide{idx}.png")
    print(OUT)


if __name__ == "__main__":
    main()
