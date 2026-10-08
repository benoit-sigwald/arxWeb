"""
Convert canonical OCI AIaaS Quiet Systems architecture diagrams to optimized WebP assets for arx-consulting.com.
"""

import os
from PIL import Image

SRC_DIR = r"G:\My Drive\OCI AIaaS\docs\assets\architecture"
DEST_DIR = r"G:\My Drive\Arx Capital\web\arxWeb\assets"

MAPPING = {
    "01-platform-overview.png": [
        "01-platform-overview.webp",
        "arx-infra-architecture.webp",
        "arx-paas-service-layer.webp",
    ],
    "02-oci-service-map.png": [
        "02-oci-service-map.webp",
        "arx-paas-details.webp",
    ],
    "03-mistral-free-mode.png": [
        "03-mistral-free-mode.webp",
        "oci-component-data-flow.webp",
    ],
    "04-delivery-and-recovery.png": [
        "04-delivery-and-recovery.webp",
        "oci-migration-en.webp",
        "svc-backups.webp",
    ],
}

def convert_all():
    for src_name, targets in MAPPING.items():
        src_path = os.path.join(SRC_DIR, src_name)
        if not os.path.exists(src_path):
            print(f"Skipping {src_name}: not found")
            continue
        
        im = Image.open(src_path)
        # Convert RGBA to RGB with white background if needed
        if im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info):
            bg = Image.new("RGB", im.size, (255, 255, 255))
            if im.mode == "P":
                im = im.convert("RGBA")
            bg.paste(im, mask=im.split()[-1])
            im = bg
        else:
            im = im.convert("RGB")
            
        w, h = im.size
        print(f"Processing {src_name} ({w}x{h})...")
        
        for tgt in targets:
            out_path = os.path.join(DEST_DIR, tgt)
            im.save(out_path, "WEBP", quality=95, method=6)
            print(f"  -> Saved {tgt}")
            
            # Generate 800px variant
            base, ext = os.path.splitext(tgt)
            out_800 = os.path.join(DEST_DIR, f"{base}-800{ext}")
            h800 = int(h * (800 / w))
            im_800 = im.resize((800, h800), Image.Resampling.LANCZOS)
            im_800.save(out_800, "WEBP", quality=92, method=6)
            print(f"  -> Saved {base}-800{ext} ({800}x{h800})")

    print("Canonical Quiet Systems diagrams converted successfully!")

if __name__ == "__main__":
    convert_all()
