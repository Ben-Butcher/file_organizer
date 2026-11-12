import  shutil
from pathlib import Path

DOWNLOADS = Path.home() / "Downloads"
DRY_RUN = True

CATEGORIES = {
    "Documents": {".pdf", ".docx", ".txt", ".md", ".pptx"},
    "Pictures": {".png", "jpeg", "jpg"},
    "Music": {".mp3"},
    "Videos": {".mp4"},
    "Application Install": {".exe"},
    "Archives": {".zip"},
}

def category_for(suffix):
    for category, extension in CATEGORIES.items():
        if suffix in extension:
            return category
    return "Misc"

for item in list(DOWNLOADS.iterdir()):
    if not item.is_file():
        continue
    if item.resolve() == Path(__file__).resolve():
        continue

    destination_folder = DOWNLOADS / category_for(item.suffix.lower())
    destination = destination_folder / item.name

    if destination.exists():
        print(f"Skip (already exist): {destination}")
        continue

    if not DRY_RUN:
         destination_folder.mkdir(exist_ok=True)
         shutil.move(item, destination)