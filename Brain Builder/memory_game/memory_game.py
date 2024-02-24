import pygame, os, random

pygame.init()


screen_width = 1040
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")
# FPS
FPS = 60
clock = pygame.time.Clock()

# COLORS
WHITE = (255, 255, 255)
CREAM = (255, 252, 213)
BLACK = (0, 0, 0)
TILE_COLOR = (244, 177, 131)



class Tile(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        super().__init__()

        self.name = filename.split('.')[0]

        self.original_image = pygame.image.load('memory_game/images/aliens/' + filename)

        self.back_image = pygame.image.load('memory_game/images/aliens/' + filename)
        pygame.draw.rect(self.back_image, TILE_COLOR, self.back_image.get_rect())

        self.image = self.back_image
        self.rect = self.image.get_rect(topleft = (x, y))
        self.shown = False

    def update(self):
        self.image = self.original_image if self.shown else self.back_image

    def show(self):
        self.shown = True
    def hide(self):
        self.shown = False
        
class MGame():
    def __init__(self):
        self.level = 1
        self.level_complete = False

        # aliens
        self.all_aliens = [f for f in os.listdir('memory_game/images/aliens') if os.path.join('memory_game/images/aliens', f)]

        self.img_width, self.img_height = (128, 128)
        self.padding = 20
        self.margin_top = 160
        self.cols = 4
        self.rows = 2
        self.width = 1040

        self.tiles_group = pygame.sprite.Group()

        # flipping & timing
        self.flipped = []
        self.frame_count = 0
        self.block_game = False

        # generate first level
        self.generate_level(self.level)

        # initialize video
        # self.is_video_playing = True
        # self.play = pygame.image.load('images/play.png').convert_alpha()
        # self.stop = pygame.image.load('images/stop.png').convert_alpha()
        # self.video_toggle = self.play
        # self.video_toggle_rect = self.video_toggle.get_rect(topright = (screen_width - 50, 10))
        # self.get_video()

        # initialize music
        self.is_music_playing = True
        self.sound_on = pygame.image.load('memory_game/images/speaker.png').convert_alpha()
        self.sound_off = pygame.image.load('memory_game/images/mute.png').convert_alpha()
        self.music_toggle = self.sound_on
        self.music_toggle_rect = self.music_toggle.get_rect(topright = (screen_width - 10, 10))

        # load music
        pygame.mixer.music.load('memory_game/sounds/bg-music.mp3')
        pygame.mixer.music.set_volume(.3)
        pygame.mixer.music.play()

    def update(self, event_list):
        # if self.is_video_playing:
        #     self.success, self.img = self.cap.read()

        self.user_input(event_list)
        self.draw()
        self.check_level_complete(event_list)

    def check_level_complete(self, event_list):
        if not self.block_game:
            for event in event_list:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for tile in self.tiles_group:
                        if tile.rect.collidepoint(event.pos):
                            self.flipped.append(tile.name)
                            tile.show()
                            if len(self.flipped) == 2:
                                if self.flipped[0] != self.flipped[1]:
                                    self.block_game = True
                                else:
                                    self.flipped = []
                                    for tile in self.tiles_group:
                                        if tile.shown:
                                            self.level_complete = True
                                        else:
                                            self.level_complete = False
                                            break
        else:
            self.frame_count += 1
            if self.frame_count == FPS:
                self.frame_count = 0
                self.block_game = False

                for tile in self.tiles_group:
                    if tile.name in self.flipped:
                        tile.hide()
                self.flipped = []


    def generate_level(self, level):
        self.aliens = self.select_random_aliens(self.level)
        self.level_complete = False
        self.rows = self.level + 1
        self.cols = 4
        self.generate_tileset(self.aliens)

    def generate_tileset(self, aliens):
        self.cols = self.rows = self.cols if self.cols >= self.rows else self.rows

        TILES_WIDTH = (self.img_width * self.cols + self.padding * 3)
        LEFT_MARGIN = RIGHT_MARGIN = (self.width - TILES_WIDTH) // 2
        #tiles = []
        self.tiles_group.empty()

        for i in range(len(aliens)):
            x = LEFT_MARGIN + ((self.img_width + self.padding) * (i % self.cols))
            y = self.margin_top + (i // self.rows * (self.img_height + self.padding))
            tile = Tile(aliens[i], x, y)
            self.tiles_group.add(tile)


    def select_random_aliens(self, level):
        aliens = random.sample(self.all_aliens, (self.level + self.level + 2))
        aliens_copy = aliens.copy()
        aliens.extend(aliens_copy)
        random.shuffle(aliens)
        return aliens

    def user_input(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.music_toggle_rect.collidepoint(pygame.mouse.get_pos()):
                    if self.is_music_playing:
                        self.is_music_playing = False
                        self.music_toggle = self.sound_off
                        pygame.mixer.music.pause()
                    else:
                        self.is_music_playing = True
                        self.music_toggle = self.sound_on
                        pygame.mixer.music.unpause()
                # if self.video_toggle_rect.collidepoint(pygame.mouse.get_pos()):
                #     if self.is_video_playing:
                #         self.is_video_playing = False
                #         self.video_toggle = self.stop
                #     else:
                #         self.is_video_playing = True
                #         self.video_toggle = self.play

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.level_complete:
                    self.level += 1
                    if self.level >= 4:
                        self.level = 1
                    self.generate_level(self.level)


    def draw(self):
        self.WHITE = (255, 255, 255)
        self.CREAM = (255, 252, 213)
        screen.fill(CREAM)
        screen_height = 800
        screen_width = 1040
        # self.screen = pygame.display.set_mode((screen_width, screen_height))
        # fonts
        title_font = pygame.font.Font('memory_game/fonts/Roboto-Black.ttf', 44)
        content_font = pygame.font.Font('memory_game/fonts/Roboto-Black.ttf', 24)

        # text
        title_text = title_font.render('Memory Game', True, BLACK)
        title_rect = title_text.get_rect(midtop = (screen_width // 2, 10))

        level_text = content_font.render('Level ' + str(self.level), True, BLACK)
        level_rect = level_text.get_rect(midtop = (screen_width // 2, 80))

        info_text = content_font.render('Find 2 of each', True, BLACK)
        info_rect = info_text.get_rect(midtop = (screen_width // 2, 120))

        # if self.is_video_playing:
        #     if self.success:
        #         screen.blit(pygame.image.frombuffer(self.img.tobytes(), self.shape, 'BGR'), (0, 120))
        #     else:
        #         self.get_video()
        # else:
            # screen.blit(pygame.image.frombuffer(self.img.tobytes(), self.shape, 'BGR'), (0, 120))

        if not self.level == 3:
            next_text = content_font.render('Level complete. Press Space for next level', True, BLACK)
        else:
            next_text = content_font.render('Congrats. You Won. Press Space to play again', True, BLACK)
        next_rect = next_text.get_rect(midbottom = (screen_width // 2, screen_height - 100))

        screen.blit(title_text, title_rect)
        screen.blit(level_text, level_rect)
        screen.blit(info_text, info_rect)
        pygame.draw.rect(screen, CREAM, (screen_width - 90, 0, 100, 50))
        # screen.blit(self.video_toggle, self.video_toggle_rect)
        screen.blit(self.music_toggle, self.music_toggle_rect)

        # draw tileset
        self.tiles_group.draw(screen)
        self.tiles_group.update()

        if self.level_complete:
            screen.blit(next_text, next_rect)

    # def get_video(self):
    #     self.cap = cv2.VideoCapture('video/earth.mp4')
    #     self.success, self.img = self.cap.read()
    #     self.shape = self.img.shape[1::-1]
    
    def run(self):
        # self.draw()
        RED = (255, 0, 0)
        self.draw()
        running = True
        while running:
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT:
                    running = False
                
            
            # Update game logic
            self.update(event_list)
            
            # Draw the game screen
            #self.draw()
            
            pygame.display.update()
            clock.tick(FPS)
        
        pygame.quit()


if __name__ == "__main__":
    GGame = MGame()
    GGame.run()
    

    
    