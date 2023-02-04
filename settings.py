class Settings:

    def __init__(self):
        self.screen_width = 1200  # screen settings
        self.screen_height = 800
        self.bg_color = (222, 184, 135)

        self.ship_speed = 1.7

        # bullets

        self.bullet_speed = 1.6
        self.bullet_width = 3  # 3
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)
        self.bullets_allowed = 3

        # aliens
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10  # 10
        self.fleet_direction = 1  # 1 is for right, -1 is for left

        #stats
        self.ship_limit = 3
