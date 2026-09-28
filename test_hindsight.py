from services.hindsight_service import retain_memory, recall_memory


memory = """
SmartShield uses SQLite because the project is currently a small prototype.
The team chose SQLite to keep development simple and avoid unnecessary database infrastructure.
"""

print("1. Storing memory...")

result = retain_memory(memory)

print("RETAIN result:", result)

print("\n2. Recalling memory...")

memories = recall_memory("Why did the SmartShield team choose SQLite?")

print("RECALL result:")
print(memories)