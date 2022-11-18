# The Particle class which supports the particle collider program.

from functions_geometric import euclidean_distance

class Particle:
	def __init__(self, position, direction, speed, radius, color):
		self.pos = position
		self.dir = direction
		self.speed = speed
		self.radius = radius
		self.color = color
		self.collision_status = False

	def guidance(self, box, particles):
		# Update direction to maintain the particle within the boundary box.
		self.boundary_update_dir(box)
		# Update direction if the particle has collided with another particle.
		self.collision_update_dir(particles)

	def boundary_update_dir(self, box):
		# box = [x_min, x_max, y_min, y_max]
		if self.pos[0] <= box[0] + self.radius and self.dir[0] < 0:
			self.dir = (self.dir[0] * -1, self.dir[1])
		elif self.pos[0] >= box[1] - self.radius and self.dir[0] > 0:
			self.dir = (self.dir[0] * -1, self.dir[1])
		if self.pos[1] <= box[2] + self.radius and self.dir[1] < 0:
			self.dir = (self.dir[0], self.dir[1] * -1)
		elif self.pos[1] >= box[3] - self.radius and self.dir[1] > 0:
			self.dir = (self.dir[0], self.dir[1] * -1)

	def collision_update_dir(self, particles):
		for particle in particles:
			if euclidean_distance(particle.pos, self.pos) <= self.radius + particle.radius and particle.pos != self.pos:
				if self.collision_status == False:
					self.collision_status == True
					x = (self.pos[0] - particle.pos[0])
					y = (self.pos[1] - particle.pos[1])
					if abs(x) >= abs(y):
						self.dir = ((x/abs(x)), (y/abs(x)))
					else:
						self.dir = ((x/abs(y)), (y/abs(y)))
					break
		else:
			self.collision_status = False

	def update_pos(self):
		self.pos = (self.pos[0] + self.dir[0] * self.speed, self.pos[1] + self.dir[1] * self.speed)
