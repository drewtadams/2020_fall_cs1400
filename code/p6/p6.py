'''
module docstring
'''
from math import hypot
from random import choices, seed
from statistics import stdev
from sys import argv
import turtle


def walk(walker, options, walks, trials):
    ''' . '''
    walk_coords = []

    # loop through the walks
    for walk in walks:
        final_coords = []

        # loop through the trials
        for _ in range(trials):
            x = 0
            y = 0

            # determine each step
            coords = choices(options, k=walk)
            for x_coord, y_coord in coords:
                x += x_coord
                y += y_coord
            final_coords.append((x, y))

        # determine distances and compute the avg and cv
        distances = list(map(lambda c: hypot(c[0], c[1]), final_coords))
        print_walk(walker, walk, distances)

        # append final coords to the walk coords if the walk length is <= 100
        if walk <= 100:
            walk_coords.append((walker, final_coords))

    return walk_coords


def print_walk(walker, walk, distances):
    ''' . '''
    avg = sum(distances) / len(distances)
    cv = stdev(distances) / avg

    # display results
    print(f'{walker} random walk of {walk} steps')
    print(f'Mean = {avg:.1f} CV = {cv:.1f}')
    print(f'Max = {max(distances):.1f} Min = {min(distances):.1f}')


def plot_walk(walk_coords, walkers):
    ''' . '''
    ZOOM = 5

    t = turtle.Turtle()
    t.turtlesize(0.5, 0.5, 0.5)
    turtle.speed(0)

    # loop through each set of trials
    for wc in walk_coords:
        walker = walkers[wc[0]]
        coords = wc[1]

        # start plotting
        t.pencolor(walker['color'])
        t.fillcolor(walker['color'])
        t.shape(walker['shape'])

        # loop through coords
        for coord in coords:
            t.up()
            t.goto(coord[0] * ZOOM, coord[1] * ZOOM)
            t.down()
            t.stamp()
    turtle.done()


def main():
    walkers = {
        'Pa': {
            'color': 'black',
            'pattern': [(0, 1), (0, -1), (1, 0), (-1, 0)],
            'shape': 'circle'
        },
        'Mi-Ma': {
            'color': 'green',
            'pattern': [(0, 1), (0, -2), (1, 0), (-1, 0)],
            'shape': 'square'
        },
        'Reg': {
            'color': 'red',
            'pattern': [(1, 0), (-1, 0)],
            'shape': 'arrow'
        }
    }

    seed(1234567890)

    try:
        # walks = list(map(lambda x: int(x), argv[1].split(',')))
        walks = [int(x) for x in argv[1].split(',')]
        trials = int(argv[2])
        walker = argv[3]

        # make sure the walker is correct
        if walker != 'all' and walker not in walkers:
            raise Exception(f'Invalid walker "{walker}"')

        # keep track of walks for plotting
        walk_coords = []

        # check if we're walking all or one
        if walker == 'all':
            for k, v in walkers.items():
                walk_coords += walk(k, v['pattern'], walks, trials)
        else:
            walk_coords = walk(walker, walkers[walker]['pattern'], walks, trials)

        # plot the walks
        plot_walk(walk_coords, walkers)
    except IndexError:
        pass
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
