import path from "node:path";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";

const require = createRequire("C:/Users/aksha/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/pptxgenjs/package.json");
const pptxgen = require("pptxgenjs");

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const outDir = __dirname;
const assetDir = path.join(outDir, "assets");

const pptx = new pptxgen();
pptx.layout = "LAYOUT_WIDE";
pptx.author = "Codex";
pptx.subject = "Stop Scaling Chaos - 3 Slide Test";
pptx.title = "Stop Scaling Chaos - Codex 3 Slide Test";
pptx.company = "BizAmps";
pptx.lang = "en-US";
pptx.theme = {
  headFontFace: "Arial",
  bodyFontFace: "Arial",
  lang: "en-US",
};
pptx.defineLayout({ name: "CUSTOM_WIDE", width: 13.333, height: 7.5 });
pptx.layout = "CUSTOM_WIDE";
pptx.defineSlideMaster({
  title: "DARK",
  background: { color: "030303" },
  objects: [
    { rect: { x: 0, y: 0, w: 13.333, h: 7.5, fill: { color: "030303" }, line: { color: "030303" } } },
  ],
});

const C = {
  white: "FFFFFF",
  yellow: "E7FF00",
  soft: "D6D6D6",
  dark: "030303",
  black: "000000",
};

function addImage(slide, file) {
  slide.addImage({ path: path.join(assetDir, file), x: 0, y: 0, w: 13.333, h: 7.5 });
  slide.addShape(pptx.ShapeType.rect, {
    x: 0,
    y: 0,
    w: 13.333,
    h: 1.55,
    fill: { color: C.black, transparency: 5 },
    line: { color: C.black, transparency: 100 },
  });
  slide.addShape(pptx.ShapeType.rect, {
    x: 0,
    y: 6.35,
    w: 13.333,
    h: 1.15,
    fill: { color: C.black, transparency: 10 },
    line: { color: C.black, transparency: 100 },
  });
}

function addRichTitle(slide, parts, y, size = 56) {
  slide.addText(parts, {
    x: 0.42,
    y,
    w: 12.55,
    h: 0.9,
    fontFace: "Arial",
    bold: true,
    fontSize: size,
    margin: 0,
    breakLine: false,
    fit: "shrink",
    shadow: { type: "outer", color: "000000", opacity: 0.55, blur: 2, angle: 45, distance: 1 },
  });
}

function addCaption(slide, text, y = 6.62) {
  slide.addText(text, {
    x: 0.55,
    y,
    w: 12.2,
    h: 0.48,
    fontFace: "Arial",
    bold: true,
    fontSize: 26,
    color: C.yellow,
    align: "center",
    margin: 0,
    fit: "shrink",
    shadow: { type: "outer", color: "000000", opacity: 0.65, blur: 2, angle: 45, distance: 1 },
  });
}

function addTinyTime(slide, text) {
  slide.addText(text, {
    x: 11.8,
    y: 7.12,
    w: 1.1,
    h: 0.18,
    fontFace: "Arial",
    fontSize: 7,
    color: "7A7A7A",
    align: "right",
    margin: 0,
  });
}

function addNotes(slide, lines) {
  slide.addNotes(lines.join("\n"));
}

{
  const slide = pptx.addSlide("DARK");
  addImage(slide, "slide1_founder.png");
  addRichTitle(slide, [
    { text: "Founder raises ", options: { color: C.white } },
    { text: "funding", options: { color: C.yellow } },
    { text: ".", options: { color: C.white } },
  ], 0.35, 55);
  slide.addText("SERIES A", {
    x: 4.78,
    y: 4.72,
    w: 3.65,
    h: 0.55,
    rotate: 0,
    fontFace: "Arial",
    fontSize: 30,
    bold: true,
    color: C.yellow,
    align: "center",
    margin: 0,
    fit: "shrink",
    shadow: { type: "outer", color: "000000", opacity: 0.6, blur: 2, angle: 45, distance: 1 },
  });
  addCaption(slide, "What could go wrong?");
  addTinyTime(slide, "0:00-0:07");
  addNotes(slide, [
    "Timestamp: 0:00-0:07",
    "Narration cue: A founder raises another round of funding.",
    "Animation cue: Reveal image, then headline, then caption.",
    "Change log: Rebuilt from flattened NotebookLM source; replaced source screenshot with editable headline/caption over a new visual.",
  ]);
}

{
  const slide = pptx.addSlide("DARK");
  addImage(slide, "slide2_team.png");
  addRichTitle(slide, [
    { text: "First move: ", options: { color: C.white } },
    { text: "hire SDRs", options: { color: C.yellow } },
    { text: ".", options: { color: C.white } },
  ], 0.33, 52);
  addCaption(slide, "The outbound cinematic universe begins.", 6.64);
  addTinyTime(slide, "0:07-0:18");
  addNotes(slide, [
    "Timestamp: 0:07-0:18",
    "Narration cue: Their first move? Hire two SDRs and a VP of Sales...",
    "Animation cue: Reveal SDRs, then VP Sales, then caption.",
    "Change log: Preserved the dramatic team joke, reduced clutter, and kept the punchline readable for YouTube.",
  ]);
}

{
  const slide = pptx.addSlide("DARK");
  addImage(slide, "slide3_calendar.png");
  addRichTitle(slide, [
    { text: "3 months ", options: { color: C.white } },
    { text: "later", options: { color: C.yellow } },
    { text: "...", options: { color: C.white } },
  ], 0.38, 58);
  slide.addText("Calendar: empty.", {
    x: 0.55,
    y: 5.92,
    w: 12.2,
    h: 0.45,
    fontFace: "Arial",
    bold: true,
    fontSize: 26,
    color: C.white,
    align: "center",
    margin: 0,
    shadow: { type: "outer", color: "000000", opacity: 0.65, blur: 2, angle: 45, distance: 1 },
  });
  addCaption(slide, "Pipeline looking spacious.", 6.62);
  addTinyTime(slide, "0:18-0:27");
  addNotes(slide, [
    "Timestamp: 0:18-0:27",
    "Narration cue: Three months later, their calendar is emptier than...",
    "Animation cue: Reveal calendar, then headline, then Calendar: empty, then caption.",
    "Change log: User chose empty-calendar concept over NotebookLM source slide 3, which showed burn rate going vertical.",
  ]);
}

await pptx.writeFile({ fileName: path.join(outDir, "Stop_Scaling_Chaos_Codex_3_Slide_Test.pptx") });
