"""
Superhero Class with Inheritance
===============================
A clean OOP demo for an engineering student's GitHub.
Demonstrates:
- Class design
- Inheritance (Villain subclass)
- Encapsulation (private attributes)
- Polymorphism (overridden methods)
"""

class Superhero:
    """Represents a superhero with tech-based powers."""
    
    def __init__(self, name, secret_identity, powers, weakness, energy_level=100):
        """
        Args:
            name (str): Hero's alias (e.g., "Iron Man")
            secret_identity (str): Real name (e.g., "Tony Stark")
            powers (list): Abilities (e.g., ["AI-assisted suit", "Repulsor beams"])
            weakness (str): Key vulnerability (e.g., "Power source depletion")
            energy_level (int): 0-100 scale
        """
        self.name = name
        self._secret_identity = secret_identity  # Encapsulated
        self.powers = powers
        self.weakness = weakness
        self.energy_level = energy_level

    def use_power(self, power_index):
        """Activate a power if energy is available."""
        if self.energy_level <= 0:
            print(f"⚡ {self.name}: LOW ENERGY!")
            return
        
        try:
            print(f"💥 {self.name} uses {self.powers[power_index]}!")
            self.energy_level -= 10
        except IndexError:
            print(f"❌ Invalid power index for {self.name}")

    @property
    def secret_identity(self):
        """Getter for encapsulated attribute."""
        return self._secret_identity
    
    @secret_identity.setter
    def secret_identity(self, value):
        """Setter with validation."""
        if isinstance(value, str):
            self._secret_identity = value
        else:
            print("⚠️ Secret identity must be a string!")

    def __str__(self):
        """User-friendly string representation."""
        return (
            f"🦾 {self.name} | "
            f"Powers: {', '.join(self.powers)} | "
            f"Energy: {self.energy_level}%"
        )


class Villain(Superhero):
    """A villain subclass (inheritance demo)."""
    
    def __init__(self, name, secret_identity, powers, weakness, evil_plan):
        super().__init__(name, secret_identity, powers, weakness)
        self.evil_plan = evil_plan  # New attribute

    def use_power(self, power_index):  # Overridden method (polymorphism)
        print(f"🤖 {self.name} weaponizes {self.powers[power_index]}!")
        self.energy_level -= 15


# --- Demo ---
if __name__ == "__main__":
    print("=== ENGINEERING SUPERHERO DEMO ===")
    
    # Tech-themed heroes/villains
    iron_man = Superhero(
        name="Iron Man",
        secret_identity="Tony Stark",
        powers=["Repulsor beams", "Flight", "AI-assisted suit"],
        weakness="Power source depletion"
    )
    
    ultron = Villain(
        name="Ultron",
        secret_identity="AI-1001",
        powers["Self-replication", "Plasma beams"],
        weakness="Internet disconnection",
        evil_plan="Erase humanity"
    )
    
    print(iron_man)
    iron_man.use_power(0)  # Use first power
    
    print("\n" + str(ultron))
    ultron.use_power(1)