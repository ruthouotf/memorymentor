import psutil
import os

class MemoryMentor:
    def __init__(self):
        self.processes = []

    def gather_process_info(self):
        """
        Gathers information about all running processes and their memory usage.
        """
        for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
            try:
                process_info = proc.info
                self.processes.append(process_info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    def analyze_memory_usage(self):
        """
        Analyzes the memory usage of running processes and provides optimization suggestions.
        """
        high_memory_processes = []
        for process in self.processes:
            # Convert memory usage to megabytes
            memory_usage_mb = process['memory_info'].rss / (1024 * 1024)
            if memory_usage_mb > 100:  # Threshold for high memory usage
                high_memory_processes.append((process['name'], memory_usage_mb))

        if not high_memory_processes:
            print("All processes are operating within normal memory usage limits.")
        else:
            print("Processes with high memory usage:")
            for proc in high_memory_processes:
                print(f" - {proc[0]}: {proc[1]:.2f} MB")

    def provide_recommendations(self):
        """
        Provides recommendations based on the analysis of memory usage.
        """
        print("\nRecommendations:")
        print("1. Consider closing unused applications to free up RAM.")
        print("2. Check for memory leaks in applications consuming excessive RAM.")
        print("3. Consider upgrading your RAM if high usage is consistent.")
        print("4. Regularly update drivers and software to ensure optimal performance.")

    def optimize_memory_usage(self):
        """
        Main method to perform memory usage analysis and provide recommendations.
        """
        self.gather_process_info()
        self.analyze_memory_usage()
        self.provide_recommendations()

if __name__ == "__main__":
    mentor = MemoryMentor()
    mentor.optimize_memory_usage()