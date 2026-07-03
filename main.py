from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.graphics import Rectangle, Color
from random import randint


class SnakeGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.snake = [(10, 10)]
        self.direction = (1, 0)
        self.food = (randint(0, 19), randint(0, 19))

        Clock.schedule_interval(self.update, 0.2)

    def update(self, dt):
        head_x, head_y = self.snake[0]
        dx, dy = self.direction

        new_head = (head_x + dx, head_y + dy)

        if new_head == self.food:
            self.food = (randint(0, 19), randint(0, 19))
        else:
            self.snake.pop()

        if new_head in self.snake:
            self.snake = [(10, 10)]

        self.snake.insert(0, new_head)
        self.draw()

    def draw(self):
        self.canvas.clear()

        with self.canvas:
            # comida
            Color(1, 0, 0)
            fx, fy = self.food
            Rectangle(pos=(fx * 20, fy * 20), size=(20, 20))

            # snake
            Color(0, 1, 0)
            for x, y in self.snake:
                Rectangle(pos=(x * 20, y * 20), size=(20, 20))

    # funciones de control
    def go_up(self, instance):
        self.direction = (0, 1)

    def go_down(self, instance):
        self.direction = (0, -1)

    def go_left(self, instance):
        self.direction = (-1, 0)

    def go_right(self, instance):
        self.direction = (1, 0)


class SnakeApp(App):
    def build(self):
        root = FloatLayout()

        game = SnakeGame()
        root.add_widget(game)

        # botones
        btn_up = Button(text="↑", size_hint=(.2, .15), pos_hint={"x": .4, "y": .15})
        btn_down = Button(text="↓", size_hint=(.2, .15), pos_hint={"x": .4, "y": 0})
        btn_left = Button(text="←", size_hint=(.2, .15), pos_hint={"x": .2, "y": .08})
        btn_right = Button(text="→", size_hint=(.2, .15), pos_hint={"x": .6, "y": .08})

        btn_up.bind(on_press=game.go_up)
        btn_down.bind(on_press=game.go_down)
        btn_left.bind(on_press=game.go_left)
        btn_right.bind(on_press=game.go_right)

        root.add_widget(btn_up)
        root.add_widget(btn_down)
        root.add_widget(btn_left)
        root.add_widget(btn_right)

        return root


SnakeApp().run() 
