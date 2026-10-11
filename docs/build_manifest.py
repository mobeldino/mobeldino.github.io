"""Lists every worksheet in docs/units/<level>/<book>/<unit>/ and writes docs/files.json.

Runs automatically on GitHub each time files are uploaded. You never need to run it yourself.
- An .html and a .pdf with the same name become one activity.
- The activity title is the HTML page's <title>; if there is none, it comes from the file name.
- Files are listed in name order, so start names with 1-, 2-, 3- to choose the order.
"""
import html, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
UNITS = os.path.join(HERE, "units")
OUT = os.path.join(HERE, "files.json")


def natural_key(name):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", name)]


def title_from_name(stem):
    t = re.sub(r"^\d+[\s._-]*", "", stem)          # drop an ordering prefix like "1-"
    t = re.sub(r"[_-]+", " ", t).strip()
    return (t[:1].upper() + t[1:]) if t else stem


def title_from_html(path):
    try:
        with open(path, encoding="utf-8", errors="ignore") as f:
            head = f.read(20000)
        m = re.search(r"<title[^>]*>(.*?)</title>", head, re.I | re.S)
        if m:
            t = html.unescape(re.sub(r"\s+", " ", m.group(1))).strip()
            return t or None
    except OSError:
        pass
    return None


def slug(stem):
    s = re.sub(r"[^a-z0-9]+", "-", stem.lower()).strip("-")
    return s or "activity"


manifest = {}
if os.path.isdir(UNITS):
    for level in sorted(os.listdir(UNITS)):
        for book in sorted(os.listdir(os.path.join(UNITS, level)) if os.path.isdir(os.path.join(UNITS, level)) else []):
            book_dir = os.path.join(UNITS, level, book)
            if not os.path.isdir(book_dir):
                continue
            for unit in sorted(os.listdir(book_dir)):
                unit_dir = os.path.join(book_dir, unit)
                if not os.path.isdir(unit_dir):
                    continue
                groups = {}
                for fn in os.listdir(unit_dir):
                    stem, ext = os.path.splitext(fn)
                    ext = ext.lower()
                    if ext not in (".html", ".htm", ".pdf") or fn.startswith((".", "_")):
                        continue
                    kind = "pdf" if ext == ".pdf" else "html"
                    groups.setdefault(stem, {})[kind] = fn
                items = []
                for stem in sorted(groups, key=natural_key):
                    g = groups[stem]
                    rel = f"units/{level}/{book}/{unit}/"
                    item = {"id": slug(stem)}
                    title = title_from_html(os.path.join(unit_dir, g["html"])) if "html" in g else None
                    item["title"] = title or title_from_name(stem)
                    if "html" in g:
                        item["html"] = rel + g["html"]
                    if "pdf" in g:
                        item["pdf"] = rel + g["pdf"]
                    items.append(item)
                # keep ids unique inside a unit
                seen = {}
                for it in items:
                    n = seen.get(it["id"], 0)
                    seen[it["id"]] = n + 1
                    if n:
                        it["id"] = f'{it["id"]}-{n + 1}'
                if items:
                    manifest[f"{level}/{book}/{unit}"] = items

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=1)
print(f"Listed {sum(len(v) for v in manifest.values())} activities in {len(manifest)} units -> files.json")
