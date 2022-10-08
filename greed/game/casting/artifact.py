from game.casting.actor import Actor
from game.shared.point import Point

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifact(Actor):
    def __init__(self):
        """Constructs a new Artifact."""
        self._points = 1

    def get_points(self):
        """Gets the artifact's points.

        Returns:
            points: The artifact's points.
        """
        return self._points

    def set_points(self, points):
        """Gets the artifact's points.

        Returns:
            points: The artifact's points.
        """
        return self._points