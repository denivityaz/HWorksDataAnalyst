import copy
import sys
import pygame
import random
import numpy as np

'''
Управление:
    R - рестарт
    0 - ИИ в режиме рандома
    1 - ИИ в режиме бога (minimax)
    G - смена режима 1/2 игрока
'''

# Сетапчик

# Окно
WIDTH = 800
HEIGHT = 800

# Сетка
ROWS = 3
COLS = 3
SQSIZE = WIDTH // COLS

# X O
LINE_WIDTH = 10
CIRC_WIDTH = 10
CROSS_WIDTH = 20
RADIUS = SQSIZE // 4
OFFSET = 75

# Цвета
BG_COLOR = (90,76,114)
LINE_COLOR = (232,241,249)
CIRC_COLOR = (255,84,173)
CROSS_COLOR = (0,193,223)


# Инициализация Pygame
pygame.init()

# Создание игрового окна
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Tic Tac Toe')
screen.fill( BG_COLOR )

# Иконка
ICON = pygame.image.load("Tic Tac Toe AI/assets/free-icon.png")
pygame.display.set_icon(ICON)

# Игровая доска
class Board:

    def __init__(self):
        self.squares = np.zeros( (ROWS, COLS) )
        self.empty_sqrs = self.squares # [squares]
        self.marked_sqrs = 0

    # Проверка на окончание игры и отображение выигрышной линии
    def final_state(self, show=False):
        '''
            @return 0 если победитель еще не определен
            @return 1 если победил игрок 1
            @return 2 если победил игрок 2
        '''

        # Вертикальные выигрыши
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                if show:
                    color = CIRC_COLOR if self.squares[0][col] == 2 else CROSS_COLOR
                    iPos = (col * SQSIZE + SQSIZE // 2, 20)
                    fPos = (col * SQSIZE + SQSIZE // 2, HEIGHT - 20)
                    pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)
                return self.squares[0][col]

        # Горизонтальные выигрыши
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                if show:
                    color = CIRC_COLOR if self.squares[row][0] == 2 else CROSS_COLOR
                    iPos = (20, row * SQSIZE + SQSIZE // 2)
                    fPos = (WIDTH - 20, row * SQSIZE + SQSIZE // 2)
                    pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)
                return self.squares[row][0]

        # Диагональ сверху вниз
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            if show:
                color = CIRC_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
                iPos = (20, 20)
                fPos = (WIDTH - 20, HEIGHT - 20)
                pygame.draw.line(screen, color, iPos, fPos, CROSS_WIDTH)
            return self.squares[1][1]

        # Диагональ снизу вверх
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            if show:
                color = CIRC_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
                iPos = (20, HEIGHT - 20)
                fPos = (WIDTH - 20, 20)
                pygame.draw.line(screen, color, iPos, fPos, CROSS_WIDTH)
            return self.squares[1][1]

        # Нет победы
        return 0

    # Отметка клетки игровой доски
    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1

    # Проверка, является ли клетка пустой
    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0

    # Получение списка пустых клеток
    def get_empty_sqrs(self):
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_sqr(row, col):
                    empty_sqrs.append( (row, col) )
        
        return empty_sqrs

    # Проверка, полностью ли заполнена доска
    def isfull(self):
        return self.marked_sqrs == 9

    # Проверка, пуста ли доска
    def isempty(self):
        return self.marked_sqrs == 0

# Класс для представления искусственного интеллекта
class AI:

    def __init__(self, level=1, player=2):
        self.level = level
        self.player = player

    # Рандомный выбор хода
    def rnd(self, board):
        empty_sqrs = board.get_empty_sqrs()
        idx = random.randrange(0, len(empty_sqrs))

        return empty_sqrs[idx] # (row, col)

    # Минимакс алгоритм для выбора оптимального хода
    def minimax(self, board, maximizing):
        
        # Терминальный случай
        case = board.final_state()

        # Вин игрока 1
        if case == 1:
            return 1, None # eval, move

        # Вин игрока 2
        if case == 2:
            return -1, None

        # Ничья
        elif board.isfull():
            return 0, None

        if maximizing:
            max_eval = -100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, 1)
                eval = self.minimax(temp_board, False)[0]
                if eval > max_eval:
                    max_eval = eval
                    best_move = (row, col)

            return max_eval, best_move

        elif not maximizing:
            min_eval = 100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, self.player)
                eval = self.minimax(temp_board, True)[0]
                if eval < min_eval:
                    min_eval = eval
                    best_move = (row, col)

            return min_eval, best_move

    # Главная функция оценки для выбора хода
    def eval(self, main_board):
        if self.level == 0:
            # Случайный выбор
            eval = 'random'
            move = self.rnd(main_board)
        else:
            # Выбор хода по алгоритму минимакс
            eval, move = self.minimax(main_board, False)

        print(f'ИИ выбрал отметить клетку в позиции {move} с оценкой: {eval}')

        return move # row, col

# Класс для представления игры
class Game:

    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.player = 1   #1-крестик  #2-нолик
        self.gamemode = 'ai' # pvp или ai
        self.running = True
        self.show_lines()

    # Отрисовка линий на игровом поле
    def show_lines(self):
        # Фон
        screen.fill( BG_COLOR )

        # Вертикальные линии
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - SQSIZE, 0), (WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)

        # Горизонтальные линии
        pygame.draw.line(screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQSIZE), (WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)

    # Отрисовка крестика или нолика в зависимости от текущего игрока
    def draw_fig(self, row, col):
        if self.player == 1:
            # Рисование крестика
            # Нисходящая линия
            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
            # Восходящая линия
            start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            end_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)
        
        elif self.player == 2:
            # Рисование нолика
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
            pygame.draw.circle(screen, CIRC_COLOR, center, RADIUS, CIRC_WIDTH)

    # Совершение хода игроком
    def make_move(self, row, col):
        self.board.mark_sqr(row, col, self.player)
        self.draw_fig(row, col)
        self.next_turn()

    # Переход к следующему ходу
    def next_turn(self):
        self.player = self.player % 2 + 1

    # Смена режима игры
    def change_gamemode(self):
        self.gamemode = 'ai' if self.gamemode == 'pvp' else 'pvp'

    # Проверка завершения игры
    def isover(self):
        return self.board.final_state(show=True) != 0 or self.board.isfull()

    # Сброс игры
    def reset(self):
        self.__init__()

# Основная функция
def main():

    game = Game()
    board = game.board
    ai = game.ai

    while True:
    
        # События Pygame
        for event in pygame.event.get():

            # Событие выхода
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Событие нажатия клавиши
            if event.type == pygame.KEYDOWN:

                # g - смена режима игры
                if event.key == pygame.K_g:
                    game.change_gamemode()

                # r - перезапуск игры
                if event.key == pygame.K_r:
                    game.reset()
                    board = game.board
                    ai = game.ai

                # 0 - выбор уровня AI: случайный выбор
                if event.key == pygame.K_0:
                    ai.level = 0
                
                # 1 - выбор уровня AI: минимакс
                if event.key == pygame.K_1:
                    ai.level = 1

            # Событие клика мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE
                
                # Человек отмечает клетку
                if board.empty_sqr(row, col) and game.running:
                    game.make_move(row, col)

                    if game.isover():
                        game.running = False

        # ИИ совершает ход
        if game.gamemode == 'ai' and game.player == ai.player and game.running:

            pygame.display.update()

            # Оценка и выбор хода
            row, col = ai.eval(board)
            game.make_move(row, col)

            if game.isover():
                game.running = False
            
        pygame.display.update()

main()
