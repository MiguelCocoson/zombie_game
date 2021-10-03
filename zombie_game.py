# Libraries necessary to make the code work.

import arcade
import random

#This class stores the functions that runs the game.

class GameView(arcade.Window):

    #This function initiates the variants and sprites that are going to be use to run the game.

    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)
        self.set_location(100, 100)

        #Inicial position of the character.

        self.player_x = 100
        self.player_y = 200

        #Random position of initiation of the zombie in the game.

        self.zombie_x = 1920
        self.zombie_y = random.randint(0, 500)

        #Initial position of the bullet.

        self.shoot_x = 0
        self.shoot_y = -100

        #Speed that the player can move.

        self.player_speed = 300

        #Initial movement of the character.

        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.click = False

        #Importing the sprites for the game.

        self.background = arcade.Sprite("sprites/background.png", center_x=960, center_y=560)
        self.player = arcade.Sprite("sprites/soldier.png", center_x=self.player_x, center_y=self.player_y)
        self.zombie = arcade.Sprite("sprites/zombie.png", center_x=self.zombie_x, center_y=self.zombie_y)
        self.shoot = arcade.Sprite("sprites/shoot.png", center_x=self.shoot_x, center_y=self.shoot_y)

    #Creates the GUI of the game.

    def on_draw(self):
        arcade.start_render()
        self.background.draw()
        self.shoot.draw()
        self.player.draw()
        self.zombie.draw()
    
    #Updates the position of the sprites.

    def on_update(self, delta_time):

        #Movements of the bullet and the zombies.

        self.shoot_x += 300 * delta_time
        self.zombie_x -= 200 * delta_time

        #Area that the player can move around.

        if self.right and self.player_x < 1920:
            self.player_x += self.player_speed * delta_time
        if self.left and self.player_x > 0:
            self.player_x -= self.player_speed * delta_time
        if self.up and self.player_y < 500:
            self.player_y += self.player_speed * delta_time
        if self.down and self.player_y > 0:
            self.player_y -= self.player_speed * delta_time

        #Concequence of the zombie getting shot.
        
        if self.zombie_x < self.shoot_x and self.zombie_y + 120 > self.shoot_y and self.zombie_y - 120 < self.shoot_y:
            self.zombie_x = 1920
            self.zombie_y = random.randint(0, 500)
            self.shoot_x = 0
            self.shoot_y = -100

        #Concequence of the zombie leaving the scenerio.
        
        if self.zombie_x < 0:
            self.zombie_x = 1920
            self.zombie_y = random.randint(0, 500)

        #If the zombie reaches the player, the game ends.
        
        if self.zombie_x - 10 < self.player_x and self.zombie_x + 150 > self.player_x and self.zombie_y + 120 > self.player_y and self.zombie_y - 120 < self.player_y:
            sys.exit()

        #Refresh position of the player, the zombie and the bullet.

        self.player.set_position(self.player_x, self.player_y)
        self.zombie.set_position(self.zombie_x, self.zombie_y)
        self.shoot.set_position(self.shoot_x, self.shoot_y)

    #Actions of precing keyboard keys. The player moves.

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.right = True
        if symbol == arcade.key.LEFT:
            self.left = True
        if symbol == arcade.key.UP:
            self.up = True
        if symbol == arcade.key.DOWN:
            self.down = True

    #Actions of releasing keyboard keys. The player stop moving.

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.right = False
        if symbol == arcade.key.LEFT:
            self.left = False
        if symbol == arcade.key.UP:
            self.up = False
        if symbol == arcade.key.DOWN:
            self.down = False

    #Action of pressing the left button of the mouse. The player shoots.
    
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.shoot_x = self.player_x
            self.shoot_y = self.player_y

#The game runs un a HD resolution.

GameView(1920, 1080, "My game window")
arcade.run()
