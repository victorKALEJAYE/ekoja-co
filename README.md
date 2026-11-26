# O.J. Ekoja & Co. website

A static website with no server or database, ready for any static host such as GitHub Pages.

## Pages
- `index.html`: Home
- `about.html`
- `practice-areas.html`
- `practice/*.html`: one page per practice area (9)
- `team.html`
- `team/oche-ekoja.html`
- `contact.html`

## Editing content
All page text lives in **`build.py`** (practice areas, mission, teamwork, partner profile, contact details).
The header, footer and layout are also defined there once and shared by every page.

1. Edit `build.py`.
2. Run `python build.py`. This regenerates every `.html` file.
3. Commit and push.

Styles are in `assets/css/site.css`. Behaviour (menu, slider, scroll animations, forms) is in `assets/js/site.js`.

## Adding photos
- **Homepage slideshow:** save photos as `images/hero-teamwork.jpg` and `images/hero-mission.jpg`, about 1920×1080 and under 400 KB each.
  The site uses them automatically. Until they exist, the slides show the drawn navy and gold backgrounds.
- **Team members:** add an 800×1200 portrait to `images/`, then add the person in `build.py`.

## Forms
There is no server, so forms open the visitor's email app (to ojekojaandco@gmail.com) or WhatsApp (+234 705 030 8648) with the message filled in.

## Photo credits
- `images/hero-mission.jpg`: "Statue of justice holding scales against blue background" by Sasun Bughdaryan, [Unsplash](https://unsplash.com/photos/zbQ5UaREHx4) (Unsplash License).
- `images/hero-teamwork.jpg`: law library shelf by Nasser Eledroos, [Unsplash](https://unsplash.com/photos/20fmGtxKs_I) (Unsplash License).
