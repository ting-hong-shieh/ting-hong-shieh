# Asset prompts

Created on 2026-10-09 with the built-in `imagegen` tool. Each call used the approved
`docs/reference/coastal-readme-concept.png` as its edit target. The project illustrations
requested transparent backgrounds; the hero requested an opaque background.

These are the exact prompts used. Local filesystem paths are not part of the prompts.
The final exports live in `art/`; the design guide records their use.

## Hero

```text
Use case: precise-object-edit.
Asset type: GitHub profile README hero illustration.
Input image 1 is the approved README concept and edit target.
Extract ONLY the large full-width coastal research station hero panel, which runs from immediately below the top repository filename rule to immediately above the cream-colored lower content area. The output is a landscape illustration in approximately 1.52:1 aspect ratio, edge to edge, no frame and no lower README content.
Preserve the approved artwork and composition as closely as possible: turquoise sky and sea, distant mountains and harbor, descending stone street, warm cream lab building on the right, greenery, wires, sleeping cat, coral-red postbox, small white astronaut with orange backpack in front of the open lab.
Preserve the exact large hand-lettered navy title at upper left: "Elias Shieh" and below it "A small world of things I build."
Preserve the coral button at the bottom right reading exactly "Explore my website ↗".
Do not redesign, add elements, change the art style, move the character, or include any repository header, project cards, captions or footer outside the hero. This is extraction of the approved panel as a standalone reusable image.
```

## QuantRail

```text
Use case: background-extraction. Asset type: standalone GitHub README project illustration.
Input image 1 is the approved README concept and edit target. Extract only the specified small illustration from the CURRENT EXPLORATIONS row; preserve its hand-drawn navy outlines, watercolor-like shading, warm ivory paper, muted sage and teal accents, and sunlit coastal research station mood. Reproduce the approved illustration closely, without redesigning. Output a horizontal approximately 2:1 canvas with the full object centered and comfortably inside the edges, genuinely transparent background, no colored rectangle, no borders, no heading, no caption, no labels or UI. Keep all depicted marks decorative and unreadable; this is an illustration, not evidence or a real screenshot. Target: the LEFT project illustration, the small cream-and-green vintage railcar on a short diagonal section of rails, beside an ivory research notebook with a simple graph, a pencil, loose notes, and a small leafy sprig. Exclude the right book illustration and all surrounding typography.
```

## Polish Open-Source Prose

```text
Use case: background-extraction. Asset type: standalone GitHub README project illustration.
Input image 1 is the approved README concept and edit target. Extract only the specified small illustration from the CURRENT EXPLORATIONS row; preserve its hand-drawn navy outlines, watercolor-like shading, warm ivory paper, muted sage and teal accents, and sunlit coastal research station mood. Reproduce the approved illustration closely, without redesigning. Output a horizontal approximately 2:1 canvas with the full object centered and comfortably inside the edges, genuinely transparent background, no colored rectangle, no borders, no heading, no caption, no labels or UI. Keep all depicted marks decorative and unreadable; this is an illustration, not evidence or a real screenshot. Target: the RIGHT project illustration, the open ivory notebook with decorative writing and a small blue-green coastal picture on its right page, a teal fountain pen lying diagonally across the lower left, a closed green book and small yellow notebook behind it, and a leafy sprig at the top right. Exclude the railcar and all surrounding typography.
```

