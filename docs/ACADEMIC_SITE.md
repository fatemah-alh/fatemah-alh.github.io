# Maintaining Fatemah's academic website

## Content source and updates

`Fatemah_Alhamdoosh_RenderCV_v6.yaml` is the authoritative source. It is unchanged by
the website customisation. Edit it, then run:

```bash
python bin/sync_cv.py
python bin/sync_cv.py --check
rendercv render _data/cv.yml --settings assets/rendercv/settings.yaml
bundle exec jekyll build
python bin/check_site.py
```

The sync command generates `_data/cv.yml`, `_bibliography/papers.bib`, and the downloadable `assets/bibliography/papers.bib`. Research,
Teaching, Beyond Research and CV read that structured data. About has an editorial
introduction; review it when your affiliation or research direction changes. New
publication identifiers require explicit verification and an update to the small
mapping in `bin/sync_cv.py`; unknown records fail rather than receiving invented metadata.

`_data/socials.yml` holds the profile links. The Google Scholar ID `TTTNVDAAAAAJ`
was supplied directly by Fatemah. The other profiles and email match the source CV.

## Installed architecture and compatibility

- al-folio core **1.0.15**, CV plugin **1.0.2**, Tailwind **4.1.18**, Jekyll **4.4.1**.
- Runtime layouts, includes, search and theme assets come from pinned gems.
- Jekyll Scholar renders the generated BibTeX on About and Publications.
- Research uses the CV's ongoing/completed sections directly, rather than duplicating
  them as four collection documents. The stock project collection remains in Git,
  excluded from publication along with other demo content.
- `_pages/cv.md` deliberately uses `layout: page`. The stock `layout: cv` renderer
  dispatches by fixed section names and silently drops this CV's custom experience,
  publication and research sections. Its generic fallback only handles `bullet`
  and `label/details` entries, so plain text sections disappear too.
- The stock header expects `label`, not `headline`; its education renderer supports
  `degree` but ignores `summary`; its publication renderer ignores `authors`,
  `journal` and `doi`. Its dates show only years. The content page preserves those
  fields, month precision, original section names, and the expected PhD date.
- No lossy schema conversion or gem-owned template overrides are needed. The
  complete RenderCV data remains usable for PDF generation.
- `assets/css/academic.css` contains site-specific presentation. Each content page
  loads it alongside the existing Tailwind theme. There is no local Tailwind build.

## PDF generation

Use Python **3.12 or newer** and `pip install -r requirements.txt`. RenderCV is pinned
to **2.8**, tested with the existing `--settings` command above. The existing settings
select the classic A4 design and write the linked PDF to
`assets/rendercv/rendercv_output/Fatemah_Alhamdoosh_CV.pdf`.

The original document validates with RenderCV 2.8. Python 3.11 selected the older
RenderCV 2.3, which rejects `locale.language: english` and uses a different settings
CLI; use the specified newer runtime rather than altering the source CV to suit it.

The existing `render-cv.yml` workflow watches `_data/cv.yml` and PDF configuration
files, renders the PDF, and commits it back. It does not watch the root source YAML,
so always run the sync command before a future approved commit. Regenerate the PDF
locally alongside content changes to ensure both are deployed together. No workflow
was changed. No commits, pushes or deployments were performed during customisation.

## Publication provenance

Verified on 19 November 2026:

- **EgoInertia-MI**: title, authors, year and preprint status match
  [arXiv:2607.03934](https://arxiv.org/abs/2607.03934). No conference acceptance is claimed.
  The [author's project website](https://fatemah-alh.github.io/EgoInertia-MI-Page/)
  supplies the completed-project link. Its provisional conference BibTeX was not used.
- **Pain Level Estimation From Videos…**: authors, title, journal, volume 7,
  pages 610–619, 2025 and DOI match the
  [University of Florence record](https://flore.unifi.it/handle/2158/1436380).
  The link is [10.1109/TBIOM.2025.3592836](https://doi.org/10.1109/TBIOM.2025.3592836).

Ongoing project descriptions reproduce only the high-level CV summaries.

## Photos and deployment

About uses the supplied `assets/img/prof_pic.png` unchanged. Beyond Research reserves
labelled spaces for plant and embroidery photos. Replace those placeholder elements
with your own images and descriptive alt text when ready. No stock imagery is shown.
ImageMagick processing is disabled while only the supplied PNG is used; it can be
enabled again when adding responsive image derivatives.

The production URL is `https://fatemah-alh.github.io`, with an empty `baseurl`.
Build with `bundle exec jekyll build`, without the upstream demo's `/al-folio` flag.
`deploy.yml` remains unchanged, including its production CSS purge.

Useful checks:

```bash
npm run lint:prettier
npm run lint:style-contract
bundle exec al-folio upgrade audit --no-fail
bundle exec al-folio upgrade overrides audit
```

RenderCV source files are excluded from Prettier to preserve their original formatting;
their YAML syntax and semantic consistency are checked separately. Upgrade-audit
notices in excluded demo posts do not affect the academic pages.

The Publications page provides a standard BibTeX download instead of the stock
mouse-only citation toggle. Publication controls have 44px targets, and year headings
use an accessible contrast color.

## Validation completed

- Production Jekyll build and the deployment's PurgeCSS step passed.
- YAML parsing, source/data consistency, full Prettier check, and the theme style
  contract passed. The original source YAML and deployment workflows are unchanged.
- Seven HTML pages and 176 local references passed link/asset validation, including
  the portrait, theme styles, PDF, and BibTeX. Every CV section and substantive entry
  was checked against the generated HTML.
- Chromium checks covered all six main pages at 320, 390, 768 and 1440 pixels:
  no horizontal overflow, JavaScript errors, failed local requests, or automated
  WCAG 2/2.1 A/AA violations. Mobile navigation was exercised.
- All six pages also passed automated accessibility checks in actual dark mode.
  PDF and BibTeX downloads and the theme control were exercised in the browser.
- The generated two-page PDF passed text/content checks.
- Upgrade audit: no blocking findings or local overrides; six non-blocking notices
  concern excluded starter posts. The temporary local build environment also warns
  about optional `jupyter-nbconvert`; no notebooks are published, and the unchanged
  deployment workflow installs that dependency.

Automated checks complement visual inspection; they do not constitute a complete
manual accessibility audit.
