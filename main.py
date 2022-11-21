# Creating a particle collider and exploring visualisation in Pygame.

import pygame
from class_Particle import Particle
from functions_geometric import euclidean_distance
from random import randint
from sys import exit

def main():
	# Initialising Pygame window, caption and clock.
	pygame.init()
	WIDTH, HEIGHT = 1280, 650
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Particle Collider")
	clock = pygame.time.Clock()

	# Creating the background surface.
	bg = pygame.Surface((WIDTH, HEIGHT))
	bg.fill((20, 20, 20))

	# Create the particles using the Particle class.
	particles = []
	for i in range(0, 50):
		pos = (randint(620, 660), randint(310, 340))
		speed = randint(2, 4)
		radius = 3
		particles.append(Particle(pos, (1, 1), speed, radius, (255, 255, 255)))

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		screen.blit(bg, (0, 0))

		# Draw lines between particles.
		for particle in particles:
			for point in particles:
				distance = euclidean_distance(particle.pos, point.pos)
				if distance < 225:
					color = (255 - distance, 255 - distance, 255 - distance)
					pygame.draw.aaline(screen, color, particle.pos, point.pos, 3)
		
		
		# Draw the particles.
		for particle in particles:
			pygame.draw.circle(screen, particle.color, particle.pos, particle.radius)

		# Perform guidance alterations to particle direction.
		for particle in particles:
			particle.guidance([0, WIDTH, 0, HEIGHT], particles)

		# Update the positions of the particles.
		for particle in particles:
			particle.update_pos()

		pygame.display.update()
		clock.tick(30)
	

if __name__ == "__main__":
	main()
