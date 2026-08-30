"""
reference.py -- STUDENT SKELETON for "נמלת לנגטון" (Langton's Ant).

A step UP from Game of Life. Life is a cellular automaton with no agent; here a
single ant walks the grid carrying STATE -- a position and a heading -- and the
board changes one cell at a time. Two famous surprises reward a correct build:
the motion looks chaotic for ~10,000 steps, and then, out of nowhere, the ant
starts building an endlessly repeating diagonal "highway".

Rules, each step:
  * on a WHITE cell (0): turn right, flip the cell to black, step forward one
  * on a BLACK cell (1): turn left,  flip the cell to white, step forward one

Note the contrast with Life: here the update is in place, one cell per step --
NO separate board is needed, because there is no simultaneous update.
"""
# headings: 0=up 1=right 2=down 3=left ; turning right is +1, left is -1 (mod 4)
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def make_grid(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]


def single_step(grid, ant):
    """Advance one step. Mutates `grid` in place and returns the new ant (r,c,h)."""
    # CP1: one step of Langton's Ant.
    #  - read the colour under the ant: grid[r][c]
    #  - WHITE (0): turn right (h+1), paint the cell black (1)
    #  - BLACK (1): turn left  (h-1), paint the cell white (0)
    #  - step forward one cell in the new heading; wrap with % to stay on the grid
    #  - return the new ant (r, c, h). The grid is changed in place.
    # TODO
    return ant


def run(grid, ant, steps):
    # CP2: apply single_step `steps` times, threading the ant through. Return the
    #      final ant. (The grid keeps changing in place.)
    # TODO
    return ant


def count_black(grid):
    # CP3: how many black cells (value 1) are on the grid.
    # TODO
    return 0


def find_highway(grid, ant, max_steps=20000):
    """Detect when the ant enters the highway: the point after which its heading
    sequence becomes periodic with period 104. Returns (onset_step, period) or
    (None, None) if not found within max_steps."""
    # CP4 (advanced): the ant eventually enters a "highway" -- its motion becomes
    #      periodic. Run steps while recording the ant's heading each step, and
    #      find the point after which the heading sequence repeats with a fixed
    #      period. Return (onset_step, period), or (None, None) if not found.
    #      Hint: the period is small and constant; compare recent windows of
    #      headings to earlier ones.
    # TODO
    return None, None


if __name__ == "__main__":
    g = make_grid(400, 400)
    ant = (200, 200, 0)
    onset, period = find_highway([row[:] for row in g], (200, 200, 0))
    print("highway onset ~ step", onset, "| period", period)
    ant = run(g, (200, 200, 0), 11000)
    print("black cells after 11000 steps:", count_black(g), "| ant:", ant)
