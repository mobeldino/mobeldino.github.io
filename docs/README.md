# Unlock practice site

Live at **https://mobeldino.github.io/** (everything lives in the `docs` folder).

## Teacher mode
Open `https://mobeldino.github.io/?teacher` once on each device you use. Lesson and book pages then show QR buttons, and the **QR codes** button prints a sheet for every level. Students never see these buttons. To switch them off on a device, open the site with `?student`.

## Adding a lesson
1. Upload the files to `docs/units/unlock-1/rw/lesson-4/` (use `ls` for Listening & Speaking).
   Quick link: github.com/mobeldino/mobeldino.github.io/upload/main/docs
2. Open `docs/content.json` → ✏️ → find the right level and book → add a lesson to its `"lessons"` list:

```json
{
  "id": "lesson-4",
  "title": "Lesson 4",
  "note": "Optional one-line description",
  "html": "units/unlock-1/rw/lesson-4/worksheet.html",
  "pdf": "units/unlock-1/rw/lesson-4/worksheet.pdf"
}
```
3. **Commit changes**. The site updates in about a minute.

Tips
- Lessons in a list are separated by a comma.
- A lesson with no `html`/`pdf` shows "Coming soon", so you can print its QR code early.
- Don't change an `id` after printing its QR code. Titles can change any time.
- Titles like "Unit 3: Food" work too.
