# Shuvo's Geographies

An interactive knowledge graph of my life in geography: the places, schools, workplaces, people, projects, methods and lessons that shaped how I read the world spatially.

**Live site:** https://shuvo-srs.github.io/shuvos-geographies/

## What it shows

- **Web**: the full graph. Click any node to spread its connections around it and see its route to the centre.
- **Convergence**: rings from where things happened (outside) to what they add up to (centre).
- **Timeline**: 1998 → 2027, left to right.
- **Position**: every node placed on two axes, technical ↔ interpretive and physical ↔ social, with the centre of gravity traced across four periods. The scores are an approximate reading.

Seven strands (the river, learning to see spatially, science with people, geography inside climate models, GIS as infrastructure, stories and critique, many homes) can be followed from the sidebar. Groups of people show their names on hover or click.

## Sources

Two CVs, the LinkedIn profile, the 2023 StoryMap *Story of a Space Interpreter*, the Choroscape About page, and the 16-chapter *My Life in Map* GeoJSON in `data/`.

## Editing

Nodes, links, strands and position scores live in `src/template.html`. The life-map chapters come from `data/my_life_in_map.geojson`. After editing either, run:

```
python3 build.py
```

which writes `index.html`. The page is static (D3 from cdnjs, Google Fonts) and needs no build tools beyond Python.
