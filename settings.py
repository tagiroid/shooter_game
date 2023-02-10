class Settings:

    def __init__(self):
        self.screen_width = 1200  # screen settings
        self.screen_height = 800
        self.bg_color = (222, 184, 135)

        self.ship_speed = 1.7

        # bullets

        self.bullet_speed = 1.6
        self.bullets_allowed = 3

        # aliens
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10  # 10
        self.fleet_direction = 1  # 1 is for right, -1 is for left
        self.speedup_scale = 1.3
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

        # stats
        self.ship_limit = 3

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0

        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
