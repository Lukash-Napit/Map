import folium

map = folium.Map()
map.save("Map.html")

latitude_of_everest = 27.9881
longitude_of_everest = 86.9250

folium.CircleMarker(
        location=[latitude_of_everest, longitude_of_everest],
        radius=5,
        color="red",
        fill=True
    ).add_to(map)
map.save("Map.html")
