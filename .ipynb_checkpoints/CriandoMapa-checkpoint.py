import folium
import json

br_estados = 'br_states.json'
geo_json_data = json.load(open(br_estados))

mapa = folium.Map(
    width=600, height=400,
    location=[-15.77972, -47.92972],
    zoom_start=3
)
folium.GeoJson(
    geo_json_data,
    style_function=lambda feature: {
        'fillColor': 'green',
        'color': 'darkred',
        'weight': 0.5,
    }
).add_to(mapa)
mapa