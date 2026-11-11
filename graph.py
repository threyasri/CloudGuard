
import csv
import matplotlib.pyplot as plt

timestamps = []
cpu_values = []
memory_values = []

# Read monitoring history
with open("monitoring_history.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        timestamps.append(row["Timestamp"])
        cpu_values.append(float(row["CPU Usage"]))
        memory_values.append(float(row["Memory Usage"]))

# Keep the latest 30 records
timestamps = timestamps[-30:]
cpu_values = cpu_values[-30:]
memory_values = memory_values[-30:]

# Create CPU graph
plt.figure(figsize=(10, 5))
plt.plot(cpu_values, marker="o", label="CPU Usage")
plt.title("CloudGuard - CPU Monitoring")
plt.xlabel("Monitoring Records")
plt.ylabel("CPU Usage (%)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("cpu_graph.png")
plt.close()

# Create memory graph
plt.figure(figsize=(10, 5))
plt.plot(memory_values, marker="o", label="Memory Usage")
plt.title("CloudGuard - Memory Monitoring")
plt.xlabel("Monitoring Records")
plt.ylabel("Memory Usage (%)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("memory_graph.png")
plt.close()

print("Monitoring graphs generated successfully!")
print("Files created: cpu_graph.png and memory_graph.png")
