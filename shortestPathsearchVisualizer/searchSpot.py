# import statements
import pygame
from pygame.locals import *

# initializing the pygame
pygame.init()

# colors
white = (255, 255, 255)  # background
black = (0, 0, 0)   # barrier
red = (255, 0, 0)  # start node
green = (0, 255, 0)  # neighbours
yellow = (255, 255, 0)  # path
grey = (192, 192, 192)  # grid lines
aqua = (0, 255, 255)  # end node

# window set up
# window dimensions
width = 600
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("SEARCH ALGORITHM")


# class spots
class Spot:
    def __init__(self, color=None, position=None):
        self.number_of_spots = 50
        self.spot_dimension = width // self.number_of_spots
        self.color = color
        self.startNode_isDrawn = 0
        self.endNode_isDrawn = 0
        self.barrier_canBeDrawn = 0
        self.barrier = []
        self.new_barrier = []
        self.position = position  # for getting position

        self.open_list = []  # contains checking spots
        self.closed_list = []  # contains checked spots
        self.lst_neighbours = []  # contains the neighbours of current element
        self.start_algo = False
        self.count = -1
        self.end = 0

    def make_Closed(self):
        self.color = yellow

    def make_Open(self):
        self.color = green

    def make_barrier(self):
        self.color = black

    def make_startNode(self):
        self.color = red

    def make_endNode(self):
        self.color = aqua

    def Remove(self):
        self.color = white

    def Reset(self):
        self.color = white
        self.startNode_isDrawn = 0
        self.endNode_isDrawn = 0
        self.barrier_canBeDrawn = 0
        self.barrier = []
        self.new_barrier = []
        self.position = None

        self.open_list = []
        self.closed_list = []
        self.lst_neighbours = []
        self.start_algo = False
        self.count = -1
        self.end = 0

    def draw_spot(self, x, y):
        pygame.draw.rect(window, self.color, (x, y, self.spot_dimension, self.spot_dimension))


# variables
spot = Spot()
barrier = Spot()  # for drawing barrier rect
start = Spot()  # for drawing starting rect
end = Spot()  # for drawing end rect
pos = None  # for mouse position after click
mouse_x = 0
mouse_y = 0


def algorithm():
    # clear neighbours list at each iteration
    spot.lst_neighbours.clear()

    # current node will be elements in open list
    current_node = spot.open_list[spot.count]

    # append neighbours if it is not barrier
    if 0 < current_node[0] < width - spot.spot_dimension and barrier.barrier.count([current_node[0] + spot.spot_dimension, current_node[1]]) == 0:
        spot.lst_neighbours.append([current_node[0] + spot.spot_dimension, current_node[1]])
    if 0 < current_node[0] < height - spot.spot_dimension and barrier.barrier.count([current_node[0] - spot.spot_dimension, current_node[1]]) == 0:
        spot.lst_neighbours.append([current_node[0] - spot.spot_dimension, current_node[1]])
    if 0 < current_node[0] < height - spot.spot_dimension and barrier.barrier.count([current_node[0], current_node[1] + spot.spot_dimension]) == 0:
        spot.lst_neighbours.append([current_node[0], current_node[1] + spot.spot_dimension])
    if 0 < current_node[0] < height - spot.spot_dimension and barrier.barrier.count([current_node[0], current_node[1] - spot.spot_dimension]) == 0:
        spot.lst_neighbours.append([current_node[0], current_node[1] - spot.spot_dimension])
    if current_node[0] == 0 and barrier.barrier.count([current_node[0] + spot.spot_dimension, current_node[1]]) == 0:
        spot.lst_neighbours.append([current_node[0] + spot.spot_dimension, current_node[1]])
    if current_node[1] == 0 and barrier.barrier.count([current_node[0], current_node[1] + spot.spot_dimension]) == 0:
        spot.lst_neighbours.append([current_node[0], current_node[1] + spot.spot_dimension])
    if current_node[0] == width - spot.spot_dimension and barrier.barrier.count([current_node[0] - spot.spot_dimension, current_node[1]]) == 0:
        spot.lst_neighbours.append([current_node[0] - spot.spot_dimension, current_node[1]])
    if current_node[1] == height - spot.spot_dimension and barrier.barrier.count([current_node[0], current_node[1] - spot.spot_dimension]) == 0:
        spot.lst_neighbours.append([current_node[0], current_node[1] - spot.spot_dimension])

    # remove start node from open_list
    if len(spot.open_list) == 1:
        spot.closed_list.append(spot.open_list[0])
        spot.open_list.pop(0)

    # stop if end point is found
    if spot.open_list.count(end.position) == 1:
        spot.lst_neighbours.clear()
        spot.end = 1

    # append neighbours to open_list
    if len(spot.lst_neighbours) != 0:
        for item in spot.lst_neighbours:
            # append items of neighbours to open list
            if spot.open_list.count(item) == 0:
                spot.open_list.append(item)

    # draw spots which are not checked
    for checking_spot in spot.open_list:
        spot.make_Open()
        spot.draw_spot(checking_spot[0], checking_spot[1])

    # append checked spots to closed list
    if spot.end != 1:
        spot.closed_list.append(spot.open_list[spot.count])

    # draw checked spots
    for checked_spot in spot.closed_list:
        spot.make_Closed()
        spot.draw_spot(checked_spot[0], checked_spot[1])

    spot.count += 1

    return False


def start_algorithm():
    keys = pygame.key.get_pressed()
    # start if space key is pressed
    if keys[pygame.K_SPACE]:
        spot.start_algo = True
    if spot.start_algo:
        if start.position is not None and end.position is not None:
            spot.open_list.append(start.position)
            algorithm()


def drawGrid():
    # draw the grid lines
    for i in range(0, width):
        pygame.draw.line(window, grey, (0, i * spot.spot_dimension), (width, i * spot.spot_dimension))
    for j in range(0, height):
        pygame.draw.line(window, grey, (j * spot.spot_dimension, 0), (j * spot.spot_dimension, height))


def drawSpots():
    global mouse_x, mouse_y, pos

    # taking the mouse position (pos)
    if pygame.mouse.get_pressed(3):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # making correction in position
        if mouse_x / spot.spot_dimension >= int(mouse_x / spot.spot_dimension):
            mouse_x = int(mouse_x / spot.spot_dimension) * spot.spot_dimension
        if mouse_y / spot.spot_dimension >= int(mouse_y / spot.spot_dimension):
            mouse_y = int(mouse_y / spot.spot_dimension) * spot.spot_dimension
        pos = [mouse_x, mouse_y]

    # draw start and end spot if left mouse button is pressed
    if pygame.mouse.get_pressed(3)[0]:
        if start.startNode_isDrawn == 0 and start.position is None:
            start.position = pos.copy()
            start.startNode_isDrawn = 1
        if start.position != pos:
            if end.endNode_isDrawn == 0 and end.position is None:
                end.position = pos.copy()
                end.endNode_isDrawn = 1
        if pos != start.position and pos != end.position:
            if end.endNode_isDrawn == 1 and start.startNode_isDrawn == 1:
                barrier.new_barrier = pos.copy()
                if len(barrier.barrier) == 0:
                    barrier.barrier.append(barrier.new_barrier)
                elif len(barrier.barrier) != 0:
                    if barrier.barrier.count(barrier.new_barrier) != 1:
                        barrier.barrier.append(barrier.new_barrier)
                barrier.barrier_canBeDrawn = 1

    # remove the spots if right mouse button is pressed
    if pygame.mouse.get_pressed(3)[2]:
        barrier.Remove()
        start.Remove()
        end.Remove()
        if pos == start.position:
            start.startNode_isDrawn = 0
            start.position = None
            spot.Reset()
        if pos == end.position:
            end.endNode_isDrawn = 0
            end.position = None
            spot.Reset()
        if len(barrier.barrier) > 0:
            if barrier.barrier.count(pos) == 1:
                barrier.barrier.pop(barrier.barrier.index(pos))

    # removing all the spots at once
    if pygame.mouse.get_pressed(3)[1]:
        spot.Reset()
        start.Reset()
        end.Reset()
        barrier.Reset()

    # infinitely draw the spots on the window till removed by the user
    if start.startNode_isDrawn == 1:
        barrier.make_startNode()
        barrier.draw_spot(start.position[0], start.position[1])
    if end.endNode_isDrawn == 1:
        barrier.make_endNode()
        barrier.draw_spot(end.position[0], end.position[1])
    if barrier.barrier_canBeDrawn == 1:
        barrier.make_barrier()
        for i in range(0, len(barrier.barrier)):
            barrier.draw_spot(barrier.barrier[i][0], barrier.barrier[i][1])


def reDrawWindow():
    # filling background with white color
    window.fill(white)
    # functions
    start_algorithm()
    # draw the spots on screen
    drawSpots()
    # draw the grid
    drawGrid()
    # updating the display everytime
    pygame.display.update()


# main function
def mainloop():
    run = True
    # running the programme till quit
    while run:
        # handling events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # exit using escape button
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
        reDrawWindow()
    pygame.quit()


if __name__ == "__main__":
    mainloop()
