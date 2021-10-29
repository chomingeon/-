import folium
import webbrowser

latitude = 37.53013593702241
longitude = 127.1237909612999
place = folium.Map(location=[latitude, longitude], zoom_start= 8)

place_name = "하남스타필드"
latitude = 37.54573469771198
longitude = 127.22407288456121
marker=folium.Marker(location=[latitude, longitude], popup= place_name,
                    icon=folium.Icon(color='blue'))
marker.add_to(place)

place_name = "용인에버랜드"
latitude = 37.294043195125276
longitude = 127.20261942465761
marker=folium.Marker(location=[latitude, longitude], popup= place_name,
                    icon=folium.Icon(color='red'))
marker.add_to(place)

place.save('map.html')
webbrowser.open_new('map.html')
