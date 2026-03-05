import pygame
from food import Food

class Snake:
    def __init__(self, x, y, block_size):
        self.block_size = block_size
        self.body = [[x, y]]
        self.length = 1
        self.x_change = 0
        self.y_change = 0
        
    def move(self):
        head = [self.body[0][0] + self.x_change, self.body[0][1] + self.y_change]
        self.body.insert(0, head)
        if len(self.body) > self.length:
            del self.body[-1]
    
    def grow(self):
        self.length += 1
    
    def set_direction(self, x_change, y_change):
        self.x_change = x_change
        self.y_change = y_change
    
    def check_collision(self, width, height):
        head = self.body[0]
        if head[0] >= width or head[0] < 0 or head[1] >= height or head[1] < 0:
            return True
        for segment in self.body[1:]:
            if segment == head:
                return True
        return False
    
    def draw(self, surface, color):
        for segment in self.body:
            pygame.draw.rect(surface, color, [segment[0], segment[1], self.block_size, self.block_size])
    
    def get_head(self):
        return self.body[0]

class Game:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.block_size = 10
        self.speed = 15
        
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 25)
        
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        
    def show_score(self, score):
        value = self.font.render("Your Score: " + str(score), True, self.white)
        self.display.blit(value, [0, 0])
    
    def show_message(self, msg, color):
        message = self.font.render(msg, True, color)
        self.display.blit(message, [self.width / 6, self.height / 3])
    
    def run(self):
        game_over = False
        game_close = False
        
        snake = Snake(self.width / 2, self.height / 2, self.block_size)
        food = Food(self.width, self.height, self.block_size)
        
        while not game_over:
            while game_close:
                self.display.fill(self.black)
                self.show_message("You Lost! Press Q-Quit or C-Play Again", self.red)
                self.show_score(snake.length - 1)
                pygame.display.update()
                
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            self.run()
                            return
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        snake.set_direction(-self.block_size, 0)
                    elif event.key == pygame.K_RIGHT:
                        snake.set_direction(self.block_size, 0)
                    elif event.key == pygame.K_UP:
                        snake.set_direction(0, -self.block_size)
                    elif event.key == pygame.K_DOWN:
                        snake.set_direction(0, self.block_size)
            
            snake.move()
            
            if snake.check_collision(self.width, self.height):
                game_close = True
            
            self.display.fill(self.black)
            food.draw(self.display, self.red)
            snake.draw(self.display, self.green)
            self.show_score(snake.length - 1)
            pygame.display.update()
            
            if snake.get_head() == food.position:
                food.position = food.spawn()
                snake.grow()
            
            self.clock.tick(self.speed)
        
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
