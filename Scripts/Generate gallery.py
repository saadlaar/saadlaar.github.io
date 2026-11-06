
import json
from pathlib import Path
from urllib.parse import quote

GALLERY_DIR = Path("assets/images/gallery")
OUTPUT_FILE = Path("gallery.json")

SUPPORTED_FORMATS = {
    ".jpg", ".jpeg", ".png", ".webp", ".gif"
}

photos = []

GALLERY_DIR.mkdir(parents=True, exist_ok=True)

for image in sorted(
    GALLERY_DIR.iterdir(),
    key=lambda p: p.name.lower()
):
    if image.is_file() and image.suffix.lower() in SUPPORTED_FORMATS:

        caption = image.stem.replace("_", " ").replace("-", " ")
        caption = caption.title()

        photos.append({
            "src": "assets/images/gallery/" + quote(image.name),
            "alt": caption,
            "caption": caption
        })

OUTPUT_FILE.write_text(
    json.dumps(photos, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8"
)

print(f"Gallery updated: {len(photos)} photographs found.")
