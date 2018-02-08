import paka.MI6
import sys,tty,termios
class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch



def get():

        ok = False
        pos = 1
        paka.MI6.mi6_connection()
        inkey = _Getch()
        while not ok:
                paka.MI6.aff_mi6()
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
            pos -= 1
            if pos == 0:
                pos = 6
        elif k=='\x1b[B':
            pos += 1
            if pos == 7:
                pos = 1
        elif k == 13:
            paka.MI6.menu_selec()
            if pos == 6:
                ok = True
            paka.clear()


def main():
        for i in range(0,20):
                get()

if __name__=='__main__':
        main()