# Unlock practice site

Live at **https://mobeldino.github.io/** (everything lives in the `docs` folder).

## Adding worksheets (the easy way)
1. Open the site in teacher mode (`https://mobeldino.github.io/?teacher`) and go to the unit.
2. Tap **Upload files to this unit**. GitHub opens that unit's folder.
3. Drag in your files and click **Commit changes**. They appear on the site in about a minute.

How files are shown:
- `vocabulary.html` + `vocabulary.pdf` (same name) become one activity with both buttons.
- The title comes from the HTML page's title; if it has none, from the file name.
- Files are listed in name order. Start names with `1-`, `2-`, `3-` to choose the order.
- Avoid spaces in file names. Renaming a file changes its QR code.

## Teacher mode
Open `https://mobeldino.github.io/?teacher` once on each device you use. Unit and lesson pages then show their QR code, a **Show to class** button and the upload button. Students never see these. To switch teacher mode off on a device, open the site with `?student`.

## Names and covers
Edit `docs/content.json` to rename a unit (`"title": "Places"`) or add a book cover (`"cover": "covers/unlock1-rw.jpg"`).
