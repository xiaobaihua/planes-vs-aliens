class Setting:
    # 舞台设置

    def __init__(self):
        # 设置背景颜色
        self.bg_color = (230, 230, 230)
        # 设置舞台大小
        self.screen_width = 600
        self.screen_height = 400

        # 飞机移动速度
        self.ship_speed = 5

        # 子弹设置
        self.bullet_speed = 10
        self.bullet_width = 5
        self.bullet_height = 5
        self.bullet_color = (150, 0, 0)

        # 敌人设置
        self.alien_speed = 1
        self.alien_sum = 5
        self.alien_lot = 1


