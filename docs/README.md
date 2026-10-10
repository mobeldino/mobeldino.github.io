# Class Materials Site — Setup & Use

Free hosting: **GitHub Pages** (permanent, no ads, interactive HTML worksheets work properly).

## 1. Put it online (once, ~10 min)
1. Create a free account at github.com.
2. Click **+ → New repository**. Name it e.g. `english` → set **Public** → **Create repository**.
3. Click **uploading an existing file**, drag in **everything inside this folder** (index.html, content.json, assets, units) → **Commit changes**.
4. Go to **Settings → Pages** → Source: **Deploy from a branch** → Branch: **main** / **(root)** → **Save**.
5. After 1–2 minutes your site is live at `https://YOUR-USERNAME.github.io/english/`

## 2. Teacher mode (QR codes)
Open once on your phone/laptop: `https://YOUR-USERNAME.github.io/english/?teacher`
- Every lesson page now shows **Show QR code** (download as PNG for slides/handouts).
- The **QR codes** button opens a printable sheet of all units and lessons.
- Students never see these buttons. (To turn teacher mode off on a device, open the site with `?student`.)

## 3. Adding a new lesson
1. In the repository, open the `units` folder → **Add file → Upload files**.
   Type the folder path in the file name box if needed, e.g. `units/unit-2/lesson-1/`, and upload `worksheet.html` and `worksheet.pdf`.
2. Open `content.json` → click the ✏️ pencil → add the lesson:

```json
{
  "id": "lesson-3",
  "title": "Lesson 3",
  "note": "Optional short description",
  "html": "units/unit-1/lesson-3/worksheet.html",
  "pdf": "units/unit-1/lesson-3/worksheet.pdf"
}
```
3. **Commit changes**. Live in about a minute.

Tips
- Separate lessons with a comma `,` — a missing comma is the most common error.
- Leave out `"html"` or `"pdf"` if a lesson has only one file. A lesson with no files shows "coming soon", so you can print QR codes before the material is ready.
- Don't rename a unit/lesson `id` after printing its QR code — the code points to that id. Titles can change freely.
- New unit: copy a whole `{ "id": "unit-2", ... }` block inside `"units"`.
