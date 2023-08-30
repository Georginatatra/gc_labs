                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        from pyowm import OWM

api_key = "9b5cf919e87ea734278768c5d3adf1bf"

owm = OWM(api_key)

mgr = owm.weather_manager()
observation = mgr.weather_at_place("Ghana")

w = observation.weather
wind = w.wind()


humidity = w.humidity

print(f"wind: {wind} \nHumididty: {humidity}")

