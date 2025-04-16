"""
Polymorphism Demo: Engineering Vehicles
======================================
Shows how different tech vehicles implement `move()` differently.
"""

class Vehicle:
    """Base class for all vehicles (abstract)."""
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")


class AutonomousDrone(Vehicle):
    """A UAV with AI navigation."""
    def move(self):
        return "🚁 Scanning terrain and avoiding obstacles with LiDAR!"


class ElectricCar(Vehicle):
    """An EV with regenerative braking."""
    def move(self):
        return "🔋 Accelerating with 800V battery system (0-60mph in 2.5s)!"


class RoboticSubmarine(Vehicle):
    """A deep-sea exploration bot."""
    def move(self):
        return "🤖 Diving to 1000m with pressure-resistant hull!"


if __name__ == "__main__":
    print("\n=== POLYMORPHISM DEMO ===")
    
    vehicles = [
        AutonomousDrone(),
        ElectricCar(),
        RoboticSubmarine()
    ]
    
    for vehicle in vehicles:
        print(vehicle.move())  # Same method, different outputs