import pygame

pygame.init()

WIDTH = 600
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))

song = pygame.mixer.music.load("Price_tag.mp3")
pygame.mixer.music.play(-1)
sound = pygame.mixer.Sound("crash.wav")

list_words = ["Music", "Playing games", "Welcome to Kazakhstan"]
index = 0

font = pygame.font.SysFont("san serif", 72)
word = font.render(list_words[index], True, "black")
font_ = pygame.font.SysFont("san serif", 24)
nex = font_.render("Next", True, "black")
prev = font_.render("Prev", True, "black")


def next_word():
    global index, word
    index = (index + 1) % len(list_words)
    word = font.render(list_words[index], True, "black")
    sound.play()

def prev_word():
    global index, word
    index = (index - 1) % len(list_words)
    word = font.render(list_words[index], True, "black")
    sound.play()


running = True
FPS = 0
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button1.collidepoint(event.pos):
                prev_word()
            if button2.collidepoint(event.pos):
                next_word()
            
            

    screen.fill("white")

    button1 = pygame.draw.rect(screen, "gray", (WIDTH // 2 - 110, HEIGHT - 200, 100, 70), 0, 5)
    button2 = pygame.draw.rect(screen, "gray", (WIDTH // 2 + 10, HEIGHT - 200, 100, 70), 0, 5)
    screen.blit(prev, (button1.centerx - prev.get_width() // 2, button1.centery - prev.get_height() // 2))
    screen.blit(nex, (button2.centerx - nex.get_width() // 2, button2.centery - nex.get_height() // 2))
    screen.blit(word, (WIDTH // 2 - word.get_width() // 2, HEIGHT // 2 - 100))
    pygame.display.flip()
    clock.tick(FPS)

        
