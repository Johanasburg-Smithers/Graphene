import pygame as py, sys, os

def __initialise(data_set: list[int | float]) -> tuple[py.Surface, int, int, int, py.time.Clock, str, bool, py.font.Font]:
    """
    Function to initialise pygame and declare variables
    used in the dot, bar and scatter functions
    """

    if data_set == [] or type(data_set) is not list:
        print('Missing Data Parameter')
        py.quit()
        sys.exit()

    py.init()

    fps: int = 10
    time: py.time.Clock = py.time.Clock()
    width: int = 800 
    height: int = 600 
    fill_colour: str = 'white'
    run: bool = True
    font: py.font.Font = py.font.SysFont(None, 50)

    screen: py.Surface = py.display.set_mode([width, height])

    try:
        icon: py.Surface = py.image.load(f'{os.path.dirname(os.path.realpath(__file__))}\Graphene.jpg')
        py.display.set_icon(icon)
    except FileNotFoundError:
        print(f"Unable To Find Icon Image In Directory '{os.path.dirname(os.path.realpath(__file__))}'")

    py.display.set_caption('Graphene')

    return screen, width, height, fps, time, fill_colour, run, font

def __draw_menu(screen: py.Surface, width: int, height: int) -> None:
    """Function to draw the x and y axes to the pygame window"""

    py.draw.line(screen, 'black', (100, height - 100), (width - 100, height - 100), 5) # x axis
    py.draw.line(screen, 'black', (100, height - 100), (100, 100), 5) # y axis

def dot(data_set: list[int | float] = [], draw_connecting_lines: bool = True, dot_size: int = 15) -> None:
    """
    A function that creates a dot graph from a set of data
    
    :param data_set: The input data set. Raises an error if ommited
    :param draw_connecting_lines: Whether lines are drawn to connect the data points
    :param dot_size: The size of the data points
    """
    
    screen, width, height, fps, time, fill_colour, run, font = __initialise(data_set)

    while run:
        time.tick(fps)
        screen.fill(fill_colour)

        __draw_menu(screen, width, height)

        __plot_dots(screen, width, height, data_set, draw_connecting_lines, dot_size, font)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        py.display.flip()
    py.quit()

def __plot_dots(screen: py.Surface, width: int, height: int, data_set: list[int | float], draw_connecting_lines: bool, dot_size: int, font: py.font.Font) -> None:
    """Function for drawing a dot graph in the pygame window"""

    x_max_dist: int = width - 200
    y_max_dist: int = height - 200

    if isinstance(max(data_set), float):
        y_spread: float = y_max_dist / round(max(data_set) + 0.4999)
    else:
        y_spread: float = y_max_dist / max(data_set)

    point_pos: list[tuple[int]] = [(100, height - 100)]

    for c in range(len(data_set)):
        distx: float = x_max_dist / len(data_set) * (c + 1)
        disty: float = y_spread * data_set[c]
        py.draw.circle(screen, 'black', (100 + distx, height - 100 - disty), dot_size)
        py.draw.line(screen, 'black', (100 + distx, height - 115), (100 + distx, height - 85), 3)
        point_pos.append((100 + distx, height - 100 - disty))

        if len(data_set) > 12:
            font = py.font.SysFont(None, 50 - round(0.85 * len(data_set)))
            img: py.Surface = font.render(str(c + 1), True, (0, 0, 0))
            screen.blit(img, (102 + distx - (10 - 0.15 * len(data_set)) * len(str(c + 1)), height - 80))
        else:
            img: py.Surface = font.render(str(c + 1), True, (0, 0, 0))
            screen.blit(img, (102 + distx - 10 * len(str(c + 1)), height - 80))

    font = py.font.SysFont(None, 50)

    for i in range(10):
        py.draw.line(screen, 'black', (85, height - 100 - y_max_dist / 10 * (i + 1)), (115, height - 100 - y_max_dist / 10 * (i + 1)), 3)
        if str(round(round(max(data_set) + 0.4999) / 10 * (i + 1), 1))[-1] == '0':
            text: str = str(round(round(max(data_set) + 0.4999) / 10 * (i + 1)))
        else:
            text: str = str(round(round(max(data_set) + 0.4999) / 10 * (i + 1), 1))
        img: py.Surface = font.render(text, True, (0, 0, 0))
        screen.blit(img, (70 - 15 * len(text), height - 115 - y_max_dist / 10 * (i + 1)))

    if draw_connecting_lines:
        py.draw.lines(screen, 'black', False, point_pos, 5)

def bar(data_set: list[int | float] = [], bar_size: int = 30) -> None:
    """
    A function that creates a bar graph from a set of data
    
    :param data_set: The input data set. Raises an error if ommited
    :param bar_size: The size of the bars
    """
    
    screen, width, height, fps, time, fill_colour, run, font = __initialise(data_set)

    while run:
        time.tick(fps)
        screen.fill(fill_colour)

        __draw_menu(screen, width, height)

        __plot_bars(screen, width, height, data_set, bar_size, font)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        py.display.flip()
    py.quit()

def __plot_bars(screen: py.Surface, width: int, height: int, data_set: list[int | float], bar_size: int, font: py.font.Font) -> None:
    """Function for drawing a bar graph in the pygame window"""

    x_max_dist: int = width - 200
    y_max_dist: int = height - 200

    if isinstance(max(data_set), float):
        y_spread = y_max_dist / round(max(data_set) + 0.4999)
    else:
        y_spread: float = y_max_dist / max(data_set)

    for c in range(len(data_set)):
        distx: float = x_max_dist / len(data_set) * (c + 1)
        disty: float = y_spread * data_set[c]
        py.draw.line(screen, 'black', (100 + distx, height - 98), (100 + distx, height - 100 - disty), bar_size)

        if len(data_set) > 12:
            font = py.font.SysFont(None, 50 - round(0.85 * len(data_set)))
            img: py.Surface = font.render(str(c + 1), True, (0, 0, 0))
            screen.blit(img, (102 + distx - (10 - 0.15 * len(data_set)) * len(str(c + 1)), height - 80))
        else:
            img: py.Surface = font.render(str(c + 1), True, (0, 0, 0))
            screen.blit(img, (102 + distx - 10 * len(str(c + 1)), height - 80))

    font = py.font.SysFont(None, 50)

    for i in range(10):
        py.draw.line(screen, 'black', (85, height - 100 - y_max_dist / 10 * (i + 1)), (115, height - 100 - y_max_dist / 10 * (i + 1)), 3)
        if str(round(round(max(data_set) + 0.4999) / 10 * (i + 1), 1))[-1] == '0':
            text: str = str(round(round(max(data_set) + 0.4999) / 10 * (i + 1)))
        else:
            text: str = str(round(round(max(data_set) + 0.4999) / 10 * (i + 1), 1))
        img: py.Surface = font.render(text, True, (0, 0, 0))
        screen.blit(img, (70 - 15 * len(text), height - 115 - y_max_dist / 10 * (i + 1)))

def scatter(data_set: list[tuple[int | float]] = [], dot_size: int = 15) -> None:
    """
    A function that creates a scatter plot from a set of data
    
    :param data_set: The input data set as a list of tuples. Raises an error if ommited
    :param dot_size: The size of the data points
    """
    
    screen, width, height, fps, time, fill_colour, run, font = __initialise(data_set)

    while run:
        time.tick(fps)
        screen.fill(fill_colour)

        __draw_menu(screen, width, height)

        __plot_scatter(screen, width, height, data_set, dot_size, font)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        py.display.flip()
    py.quit()

def __plot_scatter(screen: py.Surface, width: int, height: int, data_set: list[int | float], dot_size: int, font: py.font.Font):
    """Function for drawing a scatter plot in the pygame window"""

    x_max_dist: int = width - 200
    y_max_dist: int = height - 200
    
    x_spread: int = x_max_dist
    x_spread = min([x_max_dist / x[0] for x in data_set if x_spread > x_max_dist / x[0]])

    y_spread: int = y_max_dist
    y_spread = min([y_max_dist / y[1] for y in data_set if y_spread > y_max_dist / y[1]])
    y_spread = y_max_dist / round(y_max_dist / y_spread + 0.4999)

    for data in data_set:
        distx: float = x_max_dist / (x_max_dist / x_spread) * data[0]
        disty: float = y_spread * data[1]
        py.draw.circle(screen, 'black', (100 + distx, height - 100 - disty), dot_size)

    for j in range(int(x_max_dist / x_spread)):
        py.draw.line(screen, 'black', (100 + x_spread * (j + 1), height - 115), (100 + x_spread * (j + 1), height - 85), 3)
        if x_max_dist / x_spread > 12:
            font = py.font.SysFont(None, 50 - round(0.85 * x_max_dist / x_spread))
            img: py.Surface = font.render(str(j + 1), True, (0, 0, 0))
            screen.blit(img, (102 + x_spread * (j + 1) - (10 - 0.15 * x_max_dist / x_spread) * len(str(j + 1)), height - 80))
        else:
            img: py.Surface = font.render(str(j + 1), True, (0, 0, 0))
            screen.blit(img, (102 + x_spread * (j + 1) - 10 * len(str(j + 1)), height - 80))

    font = py.font.SysFont(None, 50)

    for i in range(10):
        py.draw.line(screen, 'black', (85, height - 100 - y_max_dist / 10 * (i + 1)), (115, height - 100 - y_max_dist / 10 * (i + 1)), 3)
        if str(round(round(y_max_dist / y_spread + 0.4999) / 10 * (i + 1), 1))[-1] == '0':
            text: str = str(round(round(y_max_dist / y_spread + 0.4999) / 10 * (i + 1)))
        else:
            text: str = str(round(round(y_max_dist / y_spread + 0.4999) / 10 * (i + 1), 1))
        img: py.Surface = font.render(text, True, (0, 0, 0))
        screen.blit(img, (70 - 15 * len(text), height - 115 - y_max_dist / 10 * (i + 1)))

data = [(1, 4), (1, 2), (2, 1), (3, 1), (4, 2), (4, 4)]
scatter(data, dot_size = 5)

# TODO:
# - Fix plot bar and scatter functions in 
# the y axis so they are the same as in 
# the plot dot function