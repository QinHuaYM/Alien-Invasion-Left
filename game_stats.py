import json


class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()

        # 游戏刚启动时处于非活动状态
        self.game_active = False

        # 读取文件中的最高分信息
        filename = 'alien_invasion_left\High_Score.json'
        with open(filename) as f:
            self.high_score = json.load(f)


    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1


