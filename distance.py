from geopy.distance import geodesic
from geopy.geocoder import Nominatim

print(geodesic(Makola_Accra, Dansoman_Accra).miles)

geolocator = Nominatim(user_agent ="geopy")
Dansoman = geolocator.geocode("Dansoman")
Accra = 

print(location.latitude, location.longitude)


print(geodesic(makola_Accra, Dansoman_Accra).miles)
