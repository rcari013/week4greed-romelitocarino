class Locations:
    """A collection of locations."""

    def __init__(self):
        """Constructs a new Actor."""
        self._locations = []

    def append_locations(self, x, y):
        location = [x,y]
        self._locations.append(location)
        
  