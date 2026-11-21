"""Rebuild index.html from src/template.html and the life-map GeoJSON.

Usage: python3 build.py
"""
import json
from pathlib import Path

root = Path(__file__).parent
geo = json.loads((root / "data" / "my_life_in_map.geojson").read_text(encoding="utf-8"))
chapters = {}
for f in geo["features"]:
    p = f["properties"]
    chapters[p["OBJECTID"]] = {
        "t": p["title"],
        "tl": p["Timeline"],
        "d": p["desc_l"].replace("\n\n\n\n", "\n\n").strip(),
        "o": p["ord_chr"],
        "c": [round(x, 5) for x in f["geometry"]["coordinates"]],
    }
template = (root / "src" / "template.html").read_text(encoding="utf-8")
(root / "index.html").write_text(template.replace("__GEO__", json.dumps(chapters, ensure_ascii=False)), encoding="utf-8")
print("index.html rebuilt")
