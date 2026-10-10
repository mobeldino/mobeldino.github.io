# Unlock practice site

Live at **https://mobeldino.github.io/** (everything lives in the `docs` folder).

## Teacher mode
Open `https://mobeldino.github.io/?teacher` once on each device you use. Lesson and book pages then show QR buttons, and the **QR codes** button prints a sheet for every level. Students never see these buttons. To switch them off on a device, open the site with `?student`.

## Adding a worksheet
Structure: level → book (`rw` = Reading & Writing, `ls` = Listening & Speaking) → unit 1–8 → lessons.

1. Upload the files to `docs/units/unlock-1/rw/unit-3/lesson-1/`.
   Quick link: github.com/mobeldino/mobeldino.github.io/upload/main/docs
2. Open `docs/content.json` → ✏️ → find the right level → book → unit → add a lesson to that unit's `"lessons"` list:

```json
{
  "id": "lesson-1",
  "title": "Lesson 1",
  "note": "Optional one-line description",
  "html": "units/unlock-1/rw/unit-3/lesson-1/worksheet.html",
  "pdf": "units/unlock-1/rw/unit-3/lesson-1/worksheet.pdf"
}
```
3. **Commit changes**. The site updates in about a minute.

Tips
- Lessons in a list are separated by a comma.
- A lesson with no `html`/`pdf` shows "Coming soon", so you can print its QR code early.
- Don't change an `id` after printing its QR code. Titles can change any time.
- Lesson titles can be anything ("Vocabulary review"). To name a unit, change its title, e.g. `"title": "Food and culture"`.
