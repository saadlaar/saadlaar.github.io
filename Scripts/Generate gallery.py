
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

async function loadGallery() {
    try {
        const response = await fetch('./Gallery.json');

        if (!response.ok) {
            throw new Error('Failed to load Gallery.json');
        }

        const data = await response.json();

        const galleryContainer =
            document.getElementById('gallery-container');

        galleryContainer.innerHTML = data.gallery.map(item => `
            <div class="gallery-item">
                <img
                    src="${item.image}"
                    alt="${item.title}"
                    loading="lazy"
                >
                <h3>${item.title}</h3>
                <p>${item.description}</p>
            </div>
        `).join('');

    } catch (error) {
        console.error('Gallery error:', error);
    }
}

loadGallery();

