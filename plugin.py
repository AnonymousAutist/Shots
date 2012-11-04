###
# Copyright (c) 2012, xo
# All rights reserved.
#
#
###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import time

class Shots(callbacks.Plugin):
    """rip strom greatest dj alive"""

    threaded = True
    
    def shot(self, irc, msg, args):
        irc.reply("SHOTS SHOTS SHOTS SHOTS SHOTS SHOTS", prefixNick=False);
        time.sleep(1)
        for x in range(0, 5):
            irc.reply("%s" % str(5-x), prefixNick=False)
            time.sleep(1)
        irc.reply("DO IT FAGIT", prefixNick=False)

Class = Shots


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
