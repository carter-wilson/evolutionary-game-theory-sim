import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Qt4agg")
plt.ion()

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


def multi(data):
    plt.clf()
    plt.subplot(2,1,1)
    plt.plot(data['pop'])
    plt.title('Population')

    plt.subplot(2,2,3)
    plt.plot(data['biddif'][:500])
    plt.title('Bid Difference - First 500')

    plt.subplot(2,2,4)
    plt.plot(data['biddif'])
    plt.title('Bid Difference')

import json
if __name__ == '__main__':
    d = json.load(open('save1.json'))
    plot(0,d['born'])
    plot(1,d['dead'])
    plot(2,d['pop'])
    # plot(3,d['old'])
    plot(3,d['age'])
    plot(4,d['pb'])
    plot(5,d['ib'])
    plt.show()
    input()
