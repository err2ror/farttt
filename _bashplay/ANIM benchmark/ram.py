import psutil
import os
from rich.console import Console
from rich.progress import Progress
console = Console()

try:
    with Progress() as progress:
        ram_usage = progress.add_task("[cyan]RAM Usage", total=100)

        while True:
            lines = os.get_terminal_size().lines
            # Get the current memory info
            memory_info = psutil.virtual_memory()
            used_percentage = memory_info.percent
            
            # Update the progress bar
            progress.update(ram_usage, completed=used_percentage)

            # Display current RAM stats

            console.print(f"Total RAM: {memory_info.total / (1024 ** 2):.2f} MB")
            console.print(f"Used RAM: {memory_info.used / (1024 ** 2):.2f} MB")
            console.print(f"Available RAM: {memory_info.available / (1024 ** 2):.2f} MB")
            console.print(f"RAM Usage Percentage: {memory_info.percent}%\n")
            print(lines-4)
        
except KeyboardInterrupt:
    console.print("\nLive update stopped.")

