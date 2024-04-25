class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __eq__(self, other):
        """
        Overloaded equality operator (==) to compare two Location objects.
        """
        return self.latitude == other.latitude and self.longitude == other.longitude

    def __ne__(self, other):
        """
        Overloaded inequality operator (!=) to compare two Location objects.
        """
        return not self.__eq__(other)

    def __str__(self):
        """
        Overloaded string representation for Location objects.
        """
        return f"Location (Latitude: {self.latitude}, Longitude: {self.longitude})"


if __name__ == "__main__":

    loc1 = Location(37.7749, -122.4194)  # San Francisco
    loc2 = Location(37.7749, -122.4194)  # Los Angeles

    if loc1 == loc2:
        print("The locations are the same.")
    else:
        print("The locations are different.")


    given_loc = Location(40.7128, -74.0060)  # New York City


    if loc1 == given_loc:
        print(f"San Francisco is the same as the given location: {given_loc}")
    else:
        print(f"San Francisco is different from the given location: {given_loc}")
