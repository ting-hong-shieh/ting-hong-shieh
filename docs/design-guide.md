# Coastal research station

The profile is a small seaside research station: an invitation to explore Elias's
work, led by a white astronaut with an orange backpack. The approved concept is
[`reference/coastal-readme-concept.png`](reference/coastal-readme-concept.png).

The user chose this illustration on 2026-10-09. The earlier discussion also referenced
[Messenger by Abeto](https://messenger.abeto.co/) for its sense of a small world to
explore. Follow the approved illustration's detailed drawing style; do not turn the
README into a low-poly game or copy the game's assets.

## Visual language

Keep hand-drawn dark outlines, warm afternoon sunlight, lightly textured surfaces,
cream buildings, plants, a turquoise sea and sky, and the coral postbox. The lab should
feel lived in. Preserve the small astronaut's rounded white suit, dark face detail,
orange backpack, and scale within the scene.

These are working palette anchors rather than a requirement to recolor existing art:

| Role | Color |
| --- | --- |
| Sea and sky | Teal `#62C9CF` |
| Buildings and paper | Cream `#FAF7EE` |
| Postbox and invitation | Coral `#E97965` |
| Outlines and lettering | Navy `#23364A` |
| Foliage | Sage `#7D9762` |

The title is hand-lettered within the hero. All project copy and navigation use
GitHub's native text. Do not rasterize the entire README or try to load a custom font
into GitHub. Avoid badges, statistics panels, extra decorative headings, and a long
list of projects that displaces the scene.

## Layout and content

1. A full-width landscape hero, approximately 3:2, linked to `https://eliasshieh.com/`.
   The hero contains “Elias Shieh”, “A small world of things I build.”, and the coral
   “Explore my website ↗” invitation. The whole image is the link.
2. The real-text introduction: “Research tools, product experiments, and a little
   curiosity.” A real website link repeats the illustrated invitation for accessibility
   and small screens.
3. “Current explorations”: exactly two equal-width cards, with independent transparent
   illustrations, linked project names, and short real-text descriptions.
4. One compact “Merged upstream” line, with checkable pull request links and the full
   contribution ledger on the website.
5. Website, Writing, and GitHub links; the quiet sign-off “No straight line.”

The two features are QuantRail and Polish Open-Source Prose. QuantRail remains marked
as early development. Do not imply that an illustrated notebook is a product screenshot
or that its decorative chart represents measured results. The prose project description
is about testing editing restraint; do not turn it into an unsupported performance claim.

Other projects, biography, and the full contribution history live on the website. When
adding work, select the two features that best represent the requested update; do not
automatically expand the profile. Keep qualifications when shortening descriptions.

## Assets

| File | Purpose |
| --- | --- |
| `art/coastal-research-station-optimized.webp` | Full scene, title, and illustrated website invitation |
| `art/quantrail.webp` | Green railcar, rails, research notebook, pencil, and leaves |
| `art/polish-open-source-prose.webp` | Open notebook, teal pen, books, coastal picture, and leaves |
| `docs/reference/coastal-readme-concept.png` | Unmodified approved concept; visual reference, not the README itself |
| `docs/asset-prompts.md` | Exact prompts for the three current illustrations |

The three illustrations were produced with the built-in image generation tool using
the approved concept as the edit target. The outputs are close adaptations, not exact
pixel crops. The original concept is preserved separately. All three displayed assets
use WebP exports. The two project illustrations retain their transparent backgrounds.

### Image loading

On 2026-10-09, the displayed image payload was reduced from 1,116,409 to 373,896 bytes
without changing pixel dimensions. The original exports remain in `art/` as sources:
`coastal-research-station.webp`, `quantrail.png`, and `polish-open-source-prose.png`.
They are not referenced by the README and do not add to its image downloads.

| Displayed export | Dimensions | Bytes | WebP quality |
| --- | --- | --- | --- |
| `coastal-research-station-optimized.webp` | 1400 × 922 | 219,106 | 85 |
| `quantrail.webp` | 760 × 380 | 85,330 | 90 |
| `polish-open-source-prose.webp` | 760 × 380 | 69,460 | 90 |

These exports were encoded with Sharp, effort 6, and alpha quality 100 for the project
illustrations. Optimize from the retained sources rather than repeatedly recompressing
the displayed files. Inspect fine lines, lettering, and transparent edges in both themes.
Keep the displayed image payload near or below 400 KB for this layout when practical.
Changing an unused source or the reference image does not improve README loading.
Payload reduction alone does not guarantee a particular load time; GitHub response
times and the visitor's connection also matter.

Use the approved reference and current assets together for future visual changes. Match
the framing, outline weight, light direction, and palette. Change one asset at a time.
Keep a new variant beside the old one until it is inspected. Do not regenerate the hero
for a project description or link update. A future animation needs an explicit design
decision; the current profile uses a static image.

## GitHub constraints and review

The cream background in the concept is part of the mockup. The live profile uses
GitHub's native background and typography so body text remains readable in both themes.
Project illustrations have transparent backgrounds. Card titles use bold paragraph
text so long project names wrap comfortably on phones. Use supported HTML attributes,
relative image paths, and ordinary links; custom CSS, scripts, image maps, and separate
click zones within the hero are not part of this implementation.

Before publishing a change:

- Render the README through GitHub's Markdown renderer and confirm every image and link.
- Inspect a desktop width and a 375px phone width in light and dark themes. Project text
  must remain selectable and readable, and the table must not overflow horizontally.
- Confirm that the hero and both project illustrations load and have descriptive alt text.
- Check the target of every changed link. Verify merged claims against upstream PRs.
- Inspect the final diff for unrelated files, credentials, and unsupported public claims.

The previous typographic SVGs and their generator remain in the repository for reference.
They are not used by this layout; Git history also preserves the previous README.
