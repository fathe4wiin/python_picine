from alchemy.grimoire.validator import validate_ingredients
from alchemy.grimoire.spellbook import record_spell

print("=== Circular Curse Breaking ===")

print("\nTesting ingredient validation:")
print(f"validate_ingredients(\"fire air\"): {validate_ingredients('fire air')}")
print(f"validate_ingredients(\"dragon scales\"): {validate_ingredients('dragon scales')}")

print("\nTesting spell recording with validation:")
print(record_spell("Fireball", "fire air"))
print(record_spell("Dark Magic", "shadow"))

print("\nTesting late import technique:")
print(record_spell("Lightning", "air"))

print("\nCircular dependency curse avoided using late imports!")
print("All spells processed safely!")
