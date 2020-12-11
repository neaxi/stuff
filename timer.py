''' Simple countdown timer written in tkinter '''

import winsound
import tkinter as tk
from functools import partial

TICK_INTERVAL = 1   # seconds
COUNTDOWNS = [0, 0.1, 0.5, 1, 5, 10, 13, 15, 20, 23]   # minutes


def sec_to_msg(secs):
    ''' 78 -> 01:18 '''
    sec = int(secs % 60)
    mins = int(secs // 60)
    return '{:02d}:{:02d}'.format(mins, sec)


class Countdown():
    ''' class implmenting the GUI and timing functionality of the timer '''
    def __init__(self):
        self.app = tk.Tk()
        self.timeleft = 0
        self.counting = False
        self.job = None

        # initial setup
        self.layout_setup()
        self.update_display('COUNTDOWN')

    def layout_setup(self):
        ''' setup of the GUI elements and Tk window attributes '''
        self.app.title('Countdown')
        self.app.attributes('-topmost', True)   # stay on top

        self.display = tk.Label(self.app,
                                font=('OCR A Extended', 26),
                                bg='black',
                                fg='red')
        self.display.pack()

        # create button for each of the time specified in minutes
        for minute in COUNTDOWNS:
            btn = tk.Button(self.app,
                            text=minute,
                            width=2,
                            command=partial(self.btn_time, minute)
                            )
            btn.pack(side=tk.LEFT)

    def update_display(self, msg):
        ''' updates display value and ensures the value is centered '''
        self.display['text'] = '{:^11}'.format(msg)

    def done(self):
        ''' action to be performed when countdown hits 0
        AppGPFault = sound Alias for Windows "Program Failure" system sound
        '''
        self.update_display('Time\'s up!')
        winsound.PlaySound('AppGPFault', winsound.SND_ALIAS)
        self.stop()

    def stop(self):
        ''' timer reset, including jobs queued by tk.after() '''
        self.counting = False
        if self.job:
            self.app.after_cancel(self.job)
            self.job = None

    def tick(self):
        ''' action to be performed each `tick` '''
        if self.counting:
            # times up
            if self.timeleft == 0:
                self.done()
            else:
                # substract, update display, queue next call in TICK_INTERVAL
                self.timeleft = self.timeleft - TICK_INTERVAL
                self.update_display(sec_to_msg(self.timeleft))
                self.job = self.app.after(int(TICK_INTERVAL * 1000), self.tick)

    def btn_time(self, minutes):
        ''' stop any cuurent countdown and start new if minutes != 0 '''
        self.stop()
        if minutes:
            self.timeleft = minutes * 60
            self.counting = True
            self.tick()


if __name__ == '__main__':
    c = Countdown()
    c.app.mainloop()
