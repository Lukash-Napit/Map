import folium
from geopy.distance import geodesic

m = folium.Map(zoom_start=4)
m.save("Map.html")

latitude_of_everest = 27.9881
longitude_of_everest = 86.9250

latitude_of_mariana_trench = 11.3493
longitude_of_mariana_trench = 142.1996

folium.CircleMarker(
        location=[latitude_of_everest, longitude_of_everest],
        radius=5,
        color="red",
        fill=True
    ).add_to(m)

folium.CircleMarker(
        location=[latitude_of_mariana_trench, longitude_of_mariana_trench],
        radius=5,
        color="green",
        fill=True
    ).add_to(m)

co_ordinates = [latitude_of_everest, longitude_of_everest],[latitude_of_mariana_trench, longitude_of_mariana_trench]

line=folium.PolyLine(co_ordinates,
                     color="blue",
                     fill=True)
line.add_to(m)
m.save("Map.html")

print(f"Distance between Mt. Everest and Mariana Trench is: "
      f"{geodesic((latitude_of_everest, longitude_of_everest),
                  (latitude_of_mariana_trench,longitude_of_mariana_trench)).kilometers}km")
