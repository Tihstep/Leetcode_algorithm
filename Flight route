def get_itinerary(flights, current_itinerary):
    if len(flights.keys()) == 0:
        return current_itinerary
    last_stop = current_itinerary[-1]
    for key, value in flights.items():
        current_itinerary.append(value)
        if key == last_stop:
            flights.pop(key)
            return get_itinerary(flights, current_itinerary)
        else:
            current_itinerary.pop()
    return None
