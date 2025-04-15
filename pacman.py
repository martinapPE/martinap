import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Tamaño de la ventana
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Clase Pacman
class Pacman:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.size = 20

    def draw(self):
        pygame.draw.circle(screen, YELLOW, (self.x, self.y), self.size)

    def move(self, dx, dy, walls):
        new_x = self.x + dx
        new_y = self.y + dy
        if not self.check_collision(new_x, new_y, walls):
            self.x = new_x
            self.y = new_y

    def check_collision(self, new_x, new_y, walls):
        # Verificar colisiones con paredes
        for wall in walls:
            if wall.colliderect(pygame.Rect(new_x - self.size, new_y - self.size, self.size * 2, self.size * 2)):
                return True
        return False

# Función para dibujar el laberinto
def draw_walls(walls):
    for wall in walls:
        pygame.draw.rect(screen, BLUE, wall)

# Función principal
def main():
    pacman = Pacman()

    # Definir paredes del laberinto
    walls = [
        pygame.Rect(100, 0, 20, 200),
        pygame.Rect(200, 100, 200, 20),
        pygame.Rect(400, 0, 20, 200),
        pygame.Rect(100, 300, 300, 20),
        pygame.Rect(0, 200, 600, 20),
    ]

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            pacman.move(-5, 0, walls)
        if keys[pygame.K_RIGHT]:
            pacman.move(5, 0, walls)
        if keys[pygame.K_UP]:
            pacman.move(0, -5, walls)
        if keys[pygame.K_DOWN]:
            pacman.move(0, 5, walls)

        screen.fill(BLACK)
        draw_walls(walls)
        pacman.draw()
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()