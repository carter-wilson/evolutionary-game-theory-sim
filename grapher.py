import matplotlib
import matplotlib.pyplot as plt


def mypause(interval):
    backend = plt.rcParams['backend']
    if backend in matplotlib.rcsetup.interactive_bk:
        figManager = matplotlib._pylab_helpers.Gcf.get_active()
        if figManager is not None:
            canvas = figManager.canvas
            if canvas.figure.stale:
                canvas.draw()
            canvas.start_event_loop(interval)
            return

def plot(f, data, xlab='Time', ylab='', overwrite=True):
    plt.figure(f)
    if overwrite:
        plt.clf()
        plt.xlabel(xlab)
        plt.ylabel(ylab)
    plt.plot(data)
    mypause(0.001)
