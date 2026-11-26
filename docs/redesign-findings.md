# Redesign findings: A.A. Malik & Co. reference → O.J. Ekoja & Co.

Phase 1–3 report (inspection, audit, mapping). No code has been changed yet.

## 0. How the reference was inspected (and the limits)

- **The live site does not load.** `aamaliklaw.com` serves a security certificate for a different domain (`registrar-servers.com`). Browsers block it, so the live site cannot be inspected at all, by me or by visitors.
- **I used the Internet Archive's saved copies** (snapshots from April 2024 to July 2026) of the home, About, Practice Areas, a practice page (Litigation), Our Team, a lawyer profile and Contact pages.
- **The archive saved the HTML, not the styling.** Every stylesheet and image returns "not found", so the saved pages render as unstyled text. From the HTML I could recover:
  - the page structure, section order, column widths and element types,
  - the exact colour palette, background colours, paddings and offsets (stored inline),
  - the animation settings (type, duration, delays),
  - the header, footer and navigation markup.
- **I could not recover** the rendered look: exact font sizes, line heights, image crops, hover styling or the mobile layout. The site is built on a commercial theme, and its public demo (stylemixthemes.com) is blocked in this browser, so I couldn't view the styled original either.

## 1. What the reference is built with

- WordPress with the **"Consulting" theme by StylemixThemes, "New Delhi" layout**, assembled with WPBakery page builder.
- Hero: **Slider Revolution**, two full-width image slides that change every 5 s with a 5×5 tile-fade transition and arrow navigation.
- Many leftover theme demo pages (shop, events, careers, sample blog posts, placeholder testimonials). We will not reproduce any of those.

## 2. Design system (recovered values)

| Token | Reference value | Our equivalent (proposed) |
|---|---|---|
| Main colour (text, dark bands, buttons) | `#00263b` deep navy | `#0E1E3A` our navy |
| Secondary accent | `#e5452b` red-orange | `#B8913A` our gold |
| Third accent (hover, icons) | `#009aee` bright blue | `#D9B970` light gold |
| Light section background | `#f5f5f5` / `#f2f2f2` | `#F5F5F5` (adopt as is) |
| Footer text | `#80939d` grey-blue; links white, hover accent | same roles, gold hover |
| Font | Raleway (Google Fonts, 100–900) | Raleway for UI + headings (switch from Cormorant/Manrope) |
| Buttons | square corners; "outline" and "modern" styles with a right-arrow icon; medium size | same |
| Section headings | small label + large centred (or left) H2 | same |

## 3. Site structure and page templates

**Navigation (all pages):** Home · About Us · Practice Areas · Our Team · Contact Us.
**Header:** logo left (about 300 px wide), menu centre/right, social icons far right. Mobile: logo plus a hamburger toggle.
**Inner pages:** each starts with a **page title bar** (H1 plus breadcrumbs, e.g. Home › About Us › Our Team).
**Footer ("style 2", dark navy):** three columns: Quick Links · Get in Touch (address, phone, email) · Social Network, then a copyright line.

### Homepage, top to bottom
1. **Hero slider:** full-width photo slides, tile transition, arrows.
2. **Our Practice Areas** (grey `#f5f5f5` band): centred heading and **3 practice cards** (icon, title, short line, "Read more"), fading up with a 0 / 0.2 / 0.4 s stagger, then an outline button to the full list.
3. **About us:** two equal columns. Text, separator and buttons on one side; an **image offset to overlap the column edge** on the other (padding 200 / 50 / 100 px, negative margins of −130 and −60 px).
4. **Navy CTA strip:** one wide-letter-spaced line (letter-spacing 7 px, white) and an outline "Contact us" button.
5. **"Straight talk rules"** (grey band): centred heading and a grid of **icon-left value boxes** (48 px icon plus title plus one line), fading up with a stagger.
6. Testimonials carousel (theme placeholder text, not real).
7. **Our People:** the same two-column text-plus-offset-image layout as About.
8. **"Request a call back":** fixed-background photo with dark overlay (parallax), a large white H2 (44/54 px), and a short form with a practice-area dropdown and Submit.
9. **Client base:** a logo carousel.
10. Footer.

### Inner pages
- **About Us:** title bar → "OUR EXPERTISE" label, H2, body text **with a sidebar menu** (company-overview links) and a button → grey band with a practice-area icon grid.
- **Practice Areas:** title bar → grey band with an icon-box grid of every practice area.
- **Single practice area:** title bar with breadcrumbs → **left sidebar listing all practice areas** (current one highlighted) → image and body text on the right.
- **Our Team:** title bar → "Teamwork" heading, uppercase sub-line, text, separator, button and offset image → team grid.
- **Lawyer profile:** title bar → photo with name, role and bio beside it → "Our Team" row of other members (photo, name, role, excerpt, "view profile").
- **Contact:** title bar → intro line → **3 info columns** (Call us · Have any questions? · Address) → grey feedback-form band.

### Motion
- On-scroll **fadeInUp** (0.5 s, staggered by 0.2 s) and **fadeIn**.
- Hero **slider with tile transition**.
- **Fixed-background parallax** band.
- Testimonial and logo **carousels**.
- No page transitions.

## 4. Audit of our current project

- **Static site, no build step:** one `index.html` (575 lines, inline CSS and JS), `logo/` (5 SVGs and a preview page), `images/partner-1.jpg` (303 KB), deployed by pushing to GitHub `victorKALEJAYE/ekoja-co` (main).
- **Single page with anchor links:** hero → The Firm → What to expect (pillars) → Practice Areas (9) → Our People → Approach → Reach → CTA band → Contact (with a mailto/WhatsApp form and map) → footer.
- **Reusable:** logo set, colour variables, contact details, practice-area copy, the form logic (email/WhatsApp), the scroll-reveal script, the reduced-motion handling and the mobile menu.
- **To redesign:** typography (switch to Raleway), every section layout, the page split, and the title bars.

## 5. Proposed mapping (ours → reference template)

**Architecture change (recommended):** split the one page into separate pages, as the reference does. CSS and JS move into shared files (`assets/css/site.css`, `assets/js/site.js`). The site stays plain HTML with no build tools, so GitHub hosting works as now.

| Our page / section | Reference template to follow |
|---|---|
| `index.html` hero | Full-width photo slider, 2–3 slides (TEAMWORK · OUR MISSION · ABOUT US). Slide images: scales of justice, law library. |
| Practice areas (home) | Grey band, **3 cards** plus "View all practice areas" button |
| Short About (home) | Two-column text plus overlapping image, "Read more" link to About |
| CTA strip | Navy letter-spaced line plus Contact button |
| "What you can expect from us" | Icon-left value grid (heading kept, "Why clients instruct us" label removed) |
| Managing Partner (home) | Two-column "Our People" layout: photo, **OCHE THANKGOD EKOJA**, one paragraph, profile link |
| Request a call back | Parallax band and short form (sends via email / WhatsApp, as now) |
| Testimonials / client logos | **Left out** until you supply real ones (placeholders would be invented content) |
| `about.html` | Title bar → label, H2, text, sidebar menu → grey practice grid |
| `practice-areas.html` | Title bar → grey icon-box grid of all 9 areas |
| `practice/<area>.html` ×9 | Title bar → left sidebar of all areas → image and text |
| `team.html` | Title bar → Teamwork intro and offset image → team grid |
| `team/oche-ekoja.html` | Title bar → photo, name, role, bio → other team members |
| `contact.html` | Title bar → 3 info columns → grey form band and map |

## 6. Content received so far (from your notes)

- Hero slides in capital letters:
  - TEAMWORK: "At O. J. Ekoja & Co., we value collaboration and shared expertise…"
  - OUR MISSION: "To provide strategic, innovative, and result-oriented legal solutions…"
  - Second slide image: scales and/or a law library.
- Home About: "A dynamic, dedicated team of legal practitioners. The firm is distinguished by its commitment to excellence, prompt service delivery and the highest standards of professional integrity." Plus a "Read more" link.
- Home practice areas: show 3, then a link to see more.
- Managing Partner: photo, OCHE THANKGOD EKOJA, one paragraph (the rest of the write-up removed).
- "What you can expect from us": keep it, but remove the "Why clients instruct us" label.

## 7. Still needed from you

1. Hero photos (scales / law library), or approval to use licensed stock photos.
2. Any other team members (names, roles, photos, bios) for the Our Team grid.
3. Fuller text for each practice-area page, or approval to expand the current short descriptions.
4. Social media links for the header and footer.
5. Real testimonials and client logos, if you want those sections (otherwise they stay out).
6. Screenshots of aamaliklaw.com, if you have any. They are the only way to match its exact type sizes, image crops and mobile layout.
