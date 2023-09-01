import noise
import numpy as np
import matplotlib.pyplot as plt

# Configurações
width, height = 500, 500
scale = 100.0

# Geração do ruído Perlin
world = np.zeros((width, height))
for y in range(height):
    for x in range(width):
        world[x][y] = noise.pnoise2(x/scale, 
                                    y/scale, 
                                    octaves=6, 
                                    persistence=0.5, 
                                    lacunarity=2.0, 
                                    repeatx=1024, 
                                    repeaty=1024, 
                                    base=0)

# Visualização usando Matplotlib
plt.imshow(world, cmap='terrain', origin='lower')
plt.colorbar()
plt.title("Ruído Perlin")
plt.show()
