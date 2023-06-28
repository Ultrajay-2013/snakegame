import pygame
import time
import objects
from objects import player
from objects import Platform
import enemy
import tools

pygame.init()


def level5loop():
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode([screen_width, screen_height])
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    gray = (192, 192, 192)
    clock = pygame.time.Clock()
    fps = 60

    re1Img = pygame.image.load("lvl5Img/1rematch.png")
    re2Img = pygame.image.load("lvl5Img/2rematch.png")
    re3Img = pygame.image.load("lvl5Img/3rematch.png")
    re4Img = pygame.image.load("lvl5Img/4rematch.png")
    re5Img = pygame.image.load("lvl5Img/finalboss.png")

    boss1platform = [Platform([0, 450], 800, 150, "gray")]
    boss2platform = [Platform([0, 450], 800, 150, "gray"), Platform([0, 0], 150, 600, "gray"), Platform([650, 0], 150, 600, "gray")]
    boss4platform = [Platform([0, 450], 300, 150, "gray"), Platform([400, 0], 300, 150, "gray")]
    l1boss = enemy.Bosslvl1("Mobs/lvl1boss_left.png", [543, 350], [100, 134], 1000, 1000, "lvl1boss", 0.5, .8, "Mobs/1boss_right", "Mobs/1boss_left")
    minotaur_boss = enemy.Minotaur_Boss("Mobs/L2_Minotaur_Boss.png",[609, 180],[100, 100],100,100,"minotaur_boss",.8, 2.9, boss1platform)
    vampire_boss = enemy.Vampire_Boss("Mobs/Vampire.png", [609, 180], [100, 100], 100, 200, "vampire_boss", 0, 5.8, boss2platform)

    scene = "scene1"

    def scene1(screen, events, time, player):
        screen.blit(re1Img, [0, 0])
        for platform in boss1platform:
            platform.render(screen)
        player.playerfunctions(screen, events, time, boss1platform)
        l1boss.update(screen, player.projectiles, player)
        pygame.draw.rect(screen, (255, 0, 0), l1boss.damage_bar)
        pygame.draw.rect(screen, (0, 255, 0), l1boss.boss_health)
        l1boss.boss_health.width = l1boss.health

    def scene2(screen, events, time, player):
        screen.blit(re2Img, [0, 0])
        for platform in boss2platform:
            platform.render(screen)
        player.playerfunctions(screen, events, time, boss2platform)
        minotaur_boss.update(screen, player.projectiles, player, boss1platform)

    def scene3(screen, events, time, player):
        screen.blit(re3Img, [0, 0])
        for platform in boss2platform:
            platform.render(screen)
        player.playerfunctions(screen, events, time, boss2platform)
        vampire_boss.update(screen, player.projectiles, player, boss2platform)
        if vampire_boss.pos[0] <= 0:
            vampire_boss.pos[0] = 0

    isRunning = True
    while isRunning:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                isRunning = False

        time = clock.get_time() / fps
        if l1boss.health <= 0 and scene == "scene1":
            scene = "scene2"
        if scene == "scene1":
            scene1(screen, events, time, player)
        if scene == "scene2":
            scene2(screen, events, time, player)
        if scene == "scene3":
            scene3(screen, events, time, player)
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    level5loop()
