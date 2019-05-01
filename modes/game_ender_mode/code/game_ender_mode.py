from mpf.core.mode import Mode
from mpf.core.delays import DelayManager
import random

class game_ender_mode(Mode):

    def mode_init(self):
        self.log.info('game_ender_mode_mode_init')
        self.delay = DelayManager(self.machine.delayRegistry)

    def mode_start(self, **kwargs):
        self.log.info('game_ender_mode_mode_start')

        self.add_mode_event_handler('wilder_says_make_the_game_end', self.end_the_game)

    def end_the_game(self, **kwargs):
        self.machine.game.end_game()

    def mode_stop(self, **kwargs):
        self.machine.events.post('game_ender_mode_mode_ended')
        self.log.info('game_ender_mode_mode_stop')