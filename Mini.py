import pygame
from voxelpy import VoxelSpace

# Initialize Pygame
pygame.init()

# Set window size
WINDOW_SIZE = (640, 480)

# Create window
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Voxel Game")

# Initialize VoxelSpace
voxel_space = VoxelSpace(64, 64, 64, cube_size=10)

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left-click
                pos = pygame.mouse.get_pos()
                x, y, z = voxel_space.get_voxel_at(pos[0], pos[1])
                voxel_space.remove_voxel(x, y, z)
            elif event.button == 3:  # Right-click
                pos = pygame.mouse.get_pos()
                x, y, z = voxel_space.get_voxel_at(pos[0], pos[1])
                voxel_space.add_voxel(x, y, z)

    # Clear screen
    screen.fill((255, 255, 255))

    # Draw Voxels
    for x, y, z, color in voxel_space.get_all_voxels():
        pygame.draw.rect(screen, color, pygame.Rect(x*10, y*10, 10, 10))

    # Update screen
    pygame.display.flip()