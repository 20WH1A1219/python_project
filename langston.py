import pygame
import tkinter as tk

# Initialize Pygame
pygame.init()

# Simulation parameters
width, height = 800, 600
cell_size = 4
num_cells_x = width // cell_size
num_cells_y = height // cell_size

# Ant parameters
ant_x = num_cells_x // 2
ant_y = num_cells_y // 2
ant_direction = 0
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # Up, Right, Down, Left

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Create the display
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Langton's Ant")

# Create a grid to store cell states
grid = [[0] * num_cells_x for _ in range(num_cells_y)]

# Function to update the display
def update_display():
    global ant_x, ant_y, ant_direction

    current_state = grid[ant_y][ant_x]
    grid[ant_y][ant_x] = 1 - current_state  # Flip cell state
    ant_direction = (ant_direction + (1 if current_state == 0 else -1)) % 4
    dx, dy = directions[ant_direction]
    ant_x = (ant_x + dx) % num_cells_x
    ant_y = (ant_y + dy) % num_cells_y

    display.fill(white)
    for y in range(num_cells_y):
        for x in range(num_cells_x):
            color = black if grid[y][x] == 1 else white
            pygame.draw.rect(display, color, (x * cell_size, y * cell_size, cell_size, cell_size))

    pygame.draw.rect(display, (255, 0, 0), (ant_x * cell_size, ant_y * cell_size, cell_size, cell_size))
    pygame.display.update()

# Function to run the simulation loop
def run_simulation():
    global sim_running, step_count

    while sim_running:
        update_display()
        pygame.time.delay(0)  # Delay for smooth visualization
        step_count += 1
        count_label.config(text=f"Steps: {step_count}")
        root.update()  # Update the GUI

# Function to start the simulation
def start_simulation():
    global sim_running, step_count
    if not sim_running:
        sim_running = True
        step_count = 0
        count_label.config(text="Steps: 0")
        run_simulation()

# Function to stop the simulation
def stop_simulation():
    global sim_running
    sim_running = False

# Create the GUI
root = tk.Tk()
root.title("Langton's Ant Simulation")

step_count = 0
count_label = tk.Label(root, text="Steps: 0")
count_label.pack()

start_button = tk.Button(root, text="Start Simulation", command=start_simulation)
start_button.pack()

stop_button = tk.Button(root, text="Stop Simulation", command=stop_simulation)
stop_button.pack()

# Set up Pygame display and simulation variables
sim_running = False

# Run the GUI event loop
root.mainloop()
