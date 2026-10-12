
CATEGORIES = {
    "Documents": {
        ".pdf", ".doc", ".docx", ".txt", ".rtf",
        ".odt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"
    },
    "Images": {
        ".jpg", ".jpeg", ".png", ".gif", ".bmp",
        ".svg", ".webp", ".tiff"
    },
    "Videos": {
        ".mp4", ".mkv", ".avi", ".mov", ".webm"
    },
    "Audio": {
        ".mp3", ".wav", ".aac", ".flac", ".ogg"
    },
    "Archives": {
        ".zip", ".rar", ".7z", ".tar", ".gz"
    },
    "Code": {
        ".py", ".c", ".cpp", ".java", ".js",
        ".html", ".css", ".php", ".sql"
    },
    "Applications": {
        ".exe", ".msi", ".deb", ".appimage", ".apk"
    }
}


def get_category(filename):
    extension = filename.lower().rsplit(".", 1)

    if len(extension) < 2:
        return "Others"

    extension = "." + extension[-1]

    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"
