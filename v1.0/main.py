from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.core.image import Image as CoreImage
import webbrowser

KV = '''
MDScreenManager:
    Menu:
    phaseselector:
    phase1:
    phase2:    
    GameOver:
    Win:
    Creditos:

<BotoesDoMenu@MDButton>    
    style: 'filled'
    theme_width: 'Custom'
    size_hint_x: None
    width: '140dp'
    theme_bg_color: 'Custom'
    md_bg_color: '#1E88E5'

<Menu@MDScreen>:
    name: 'menu'
    md_bg_color: '#111827'
    MDFloatLayout:
        MDLabel:
            text: 'The Maze'
            color: '#FFFFFF'
            theme_font_size: 'Custom'
            font_size: '100sp'
            theme_font_name: 'Custom'
            font_name: 'utilidades/Dmitry Rastvortsev - KyivType Sans Regular.otf'
            pos_hint: {'center_x':0.5, 'center_y':0.6}
            size_hint_x: 0.8
            halign: 'center'
            
        BotoesDoMenu:
            pos_hint: {'center_x':0.5, 'center_y':0.35}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'phaseselector'
            MDButtonText:
                text:'Jogar'
                theme_font_size: 'Custom'
                pos_hint: {'center_x': .5, 'center_y': .5}
                font_size: '25sp'
                color: '#FFFFFF'
                theme_font_name: 'Custom'
                font_name: 'utilidades/JacquesFrancois-Regular.ttf'   
        BotoesDoMenu:
            pos_hint: {'center_x':0.5, 'center_y':0.27}
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'creditos'
            MDButtonText:
                text:'Creditos'
                theme_font_size: 'Custom'
                pos_hint: {'center_x': .5, 'center_y': .5}
                font_size: '25sp'
                color: '#FFFFFF'
                theme_font_name: 'Custom'
                font_name: 'utilidades/JacquesFrancois-Regular.ttf'     
        BotoesDoMenu:  
            pos_hint: {'center_x':0.5, 'center_y':0.19}
            on_press:
                app.stop()
            MDButtonText:
                text:'Sair'
                theme_font_size: 'Custom'
                pos_hint: {'center_x': .5, 'center_y': .5}
                font_size: '25sp'
                color: '#FFFFFF'
                theme_font_name: 'Custom'
                font_name: 'utilidades/JacquesFrancois-Regular.ttf'

<phaseselector@MDScreen>:
    name: 'phaseselector'
    md_bg_color: '#111827'
    MDFloatLayout:
        MDLabel:
            text: 'Selecione a fase'
            color: '#FFFFFF'
            theme_font_size: 'Custom'
            font_size: '70sp'
            theme_font_name: 'Custom'
            font_name: 'utilidades/Dmitry Rastvortsev - KyivType Sans Regular.otf'
            pos_hint: {'center_x':0.5, 'center_y':0.6}
            size_hint_x: 0.8
            halign: 'center'
        BotoesDoMenu:
            pos_hint: {'center_x':0.5, 'center_y':0.35}
            on_press:
                root.manager.current = 'phase1'
            MDButtonText:
                text:'Fase 1'
                theme_font_size: 'Custom'
                pos_hint: {'center_x': .5, 'center_y': .5}
                font_size: '25sp'
                color: '#FFFFFF'
                theme_font_name: 'Custom'
                font_name: 'utilidades/JacquesFrancois-Regular.ttf'   
        BotoesDoMenu:
            pos_hint: {'center_x':0.5, 'center_y':0.27}
            on_press:
                root.manager.current = 'phase2'
            MDButtonText:
                text:'Fase 2'
                theme_font_size: 'Custom'
                pos_hint: {'center_x': .5, 'center_y': .5}
                font_size: '25sp'
                color: '#FFFFFF'
                theme_font_name: 'Custom'
                font_name: 'utilidades/JacquesFrancois-Regular.ttf'     
        BotoesDoMenu:  
            pos_hint: {'center_x':0.5, 'center_y':0.19}
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'menu'
            MDButtonText:
                text:'Voltar'
                theme_font_size: 'Custom'
                pos_hint: {'center_x': .5, 'center_y': .5}
                font_size: '25sp'
                color: '#FFFFFF'
                theme_font_name: 'Custom'
                font_name: 'utilidades/JacquesFrancois-Regular.ttf'

<boneco>:
    source: 'utilidades/PC.png'

<phase1>:
    name: 'phase1'
    md_bg_color: '#111827'      
    MDFloatLayout:
        Maze:
            id: maze
        
        boneco:
            id: player
            allow_stretch: True
            size_hint: None, None

            x: root.width * 0.85 
            y: root.height / 2 - self.height / 2

<phase2>:
    name: 'phase2'
    md_bg_color: '#111827'  
    MDFloatLayout:
        MazePhase2:
            id: maze2
        
        boneco:
            id: player
            allow_stretch: True
            size_hint: None, None

            x: root.width * 0.85 
            y: root.height / 2 - self.height / 2

<GameOver@MDScreen>:
    name: 'fim'
    md_bg_color: '#111827'
    MDFloatLayout:
        MDLabel:
            text: 'Voce Perdeu!'
            color: '#FF000'
            theme_font_size: 'Custom'
            font_size: '100sp'
            theme_font_name: 'Custom'
            font_name: 'utilidades/Dmitry Rastvortsev - KyivType Sans Regular.otf'
            pos_hint: {'center_x':0.5, 'center_y':0.6}
            size_hint_x: 0.8
            halign: 'center'
            
        BotoesDoMenu:
            pos_hint: {'center_x':0.5, 'center_y':0.35}
            width: '200dp'
            on_press:
                root.manager.current = 'menu'
            MDButtonText:
                text:'Ir para o menu'
                theme_font_size: 'Custom'
                pos_hint: {'center_x': .5, 'center_y': .5}
                font_size: '25sp'
                color: '#FFFFFF'
                theme_font_name: 'Custom'
                font_name: 'utilidades/JacquesFrancois-Regular.ttf'
<Win@MDScreen>:
    name: 'vitoria'
    md_bg_color: '#111827'
    MDFloatLayout:
        MDLabel:
            text: 'Voce Venceu!'
            color: '#FFFFFF'
            theme_font_size: 'Custom'
            font_size: '100sp'
            theme_font_name: 'Custom'
            font_name: 'utilidades/Dmitry Rastvortsev - KyivType Sans Regular.otf'
            pos_hint: {'center_x':0.5, 'center_y':0.6}
            size_hint_x: 0.8
            halign: 'center'
            
        BotoesDoMenu:
            pos_hint: {'center_x':0.5, 'center_y':0.35}
            width: '200dp'
            on_press:
                root.manager.current = 'menu'
            MDButtonText:
                text:'Ir para o menu'
                theme_font_size: 'Custom'
                pos_hint: {'center_x': .5, 'center_y': .5}
                font_size: '25sp'
                color: '#FFFFFF'
                theme_font_name: 'Custom'
                font_name: 'utilidades/JacquesFrancois-Regular.ttf'


<Creditos@MDScreen>:
    name: 'creditos'
    md_bg_color: '#111827'
    MDFloatLayout:
        BotoesDoMenu:
            pos_hint: {'center_x':0.5, 'center_y':0.60}
            width: '235dp'
            on_press:
                app.open_link('https://github.com/brunoaudricc')
            MDButtonIcon:
                icon: 'github'
            MDButtonText:
                text:'brunoaudricc'
                theme_font_size: 'Custom'
                pos_hint: {'center_x': 0.5, 'center_y': .5}
                font_size: '25sp'
                color: '#FFFFFF'
                theme_font_name: 'Custom'
                font_name: 'utilidades/JacquesFrancois-Regular.ttf'
            
        BotoesDoMenu:
            pos_hint: {'center_x':0.5, 'center_y':0.5}
            width: '235dp'
            on_press:
                app.open_link('https://www.linkedin.com/in/bruno-audric-2143b2273/')
            MDButtonIcon:
                icon: 'linkedin'
            MDButtonText:
                text:'Bruno Audric'
                theme_font_size: 'Custom'
                pos_hint: {'center_x': .5, 'center_y': .5}
                font_size: '25sp'
                color: '#FFFFFF'
                theme_font_name: 'Custom'
                font_name: 'utilidades/JacquesFrancois-Regular.ttf'

        BotoesDoMenu:
            pos_hint: {'center_x':0.5, 'center_y':0.25}
            width: '200dp'
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'menu'
            MDButtonText:
                text:'Voltar'
                theme_font_size: 'Custom'
                pos_hint: {'center_x': .5, 'center_y': .5}
                font_size: '25sp'
                color: '#FFFFFF'
                theme_font_name: 'Custom'
                font_name: 'utilidades/JacquesFrancois-Regular.ttf'
'''

class Maze(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.labirinto = [
    [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
        self.cell_size = min((Window.width * 0.8) / len(self.labirinto[0]), Window.height / len(self.labirinto))
        self.walls = []
        self.win_cells = []
        self.wall_texture = CoreImage('utilidades/parede.png').texture
        self.path_texture = CoreImage('utilidades/chao.png').texture
        self.win_texture = CoreImage('utilidades/vitoria.png').texture
        self.draw_maze()      


    def draw_maze(self):

        self.canvas.clear()

        maze_height = len(self.labirinto) * self.cell_size
        offset_x = 0  
        offset_y = (Window.height - maze_height) / 2  

        with self.canvas:
            for row_index, row in enumerate(self.labirinto):
                for col_index, cell in enumerate(row):
                    x = offset_x + col_index * self.cell_size
                    y = offset_y + (len(self.labirinto) - row_index - 1) * self.cell_size

                    if cell == 1:  
                        Color(1, 1, 1, 1)
                        rect = Rectangle(pos=(x, y), size=(self.cell_size, self.cell_size))
                        rect.texture = self.wall_texture  

                        wall = Widget(size=(self.cell_size, self.cell_size), pos=(x, y))
                        self.add_widget(wall)
                        self.walls.append(wall)
                    elif cell == 2:
                        Color(1, 1, 1, 1)
                        rect = Rectangle(pos=(x, y), size=(self.cell_size, self.cell_size))
                        rect.texture = self.win_texture
                        
                        win_cell = Widget(size=(self.cell_size, self.cell_size), pos=(x, y))
                        self.add_widget(win_cell)
                        self.win_cells.append(win_cell)
                    else:  
                        Color(1, 1, 1, 1)
                        rect = Rectangle(pos=(x, y), size=(self.cell_size, self.cell_size))
                        rect.texture = self.path_texture  

class MazePhase2(Maze):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [2, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
        self.walls = []
        self.win_cells = []
        self.cell_size = min((Window.width * 0.8) / len(self.labirinto[0]), Window.height / len(self.labirinto))
        self.draw_maze()

class PhaseBase(MDScreen):
    def on_pre_enter(self, *args):
        Window.bind(on_key_down=self.on_key_down)
        Window.bind(on_key_up=self.on_key_up)
        Clock.schedule_interval(self.update, 1/60)
        self.reset_player_position()
        
        maze = self.ids.maze if hasattr(self.ids, 'maze') else self.ids.maze2
        cell_size = maze.cell_size
        self.ids.player.size = (cell_size * 0.6, cell_size * 0.6)
        self.ids.player.speed = self.ids.player.base_speed * cell_size * 4

    def on_leave(self, *args):
        Window.unbind(on_key_down=self.on_key_down)
        Window.unbind(on_key_up=self.on_key_up)
        Clock.unschedule(self.update)

    def update(self, dt):
        player = self.ids.player
        maze = self.ids.maze if hasattr(self.ids, 'maze') else self.ids.maze2

        new_x = player.x + player.horizontal_speed * dt
        new_y = player.y + player.vertical_speed * dt

        if not self.check_collision(new_x, player.y, maze.walls):
            player.x = new_x
        else:
            self.game_over()

        if not self.check_collision(player.x, new_y, maze.walls):
            player.y = new_y
        else:
            self.game_over()
            
        if self.check_win(player.x, player.y, maze.win_cells):
            self.win_game()

    def game_over(self):
        self.manager.current = 'fim'

    def check_collision(self, x, y, walls):
        for wall in walls:
            if (x < wall.right and x + self.ids.player.width > wall.x and
                y < wall.top and y + self.ids.player.height > wall.y):
                return True
        return False
    
    def check_win(self, x, y, win_cells):
        for win_cell in win_cells:
            if (x < win_cell.right and x + self.ids.player.width > win_cell.x and
                y < win_cell.top and y + self.ids.player.height > win_cell.y):
                return True
        return False

    def win_game(self):
        self.manager.current = 'vitoria'
    
    def reset_player_position(self):
        player = self.ids.player
        player.x = self.width * 0.85
        player.y = self.height / 2 - player.height / 2
        
    def on_key_down(self, window, key, *args):
        player = self.ids.player
        if key == 97:  # A (esquerda)
            player.horizontal_speed = -player.speed
        elif key == 100:  # D (direita)
            player.horizontal_speed = player.speed
        elif key == 119:  # W (cima)
            player.vertical_speed = player.speed
        elif key == 115:  # S (baixo)
            player.vertical_speed = -player.speed

    def on_key_up(self, window, key, *args):
        player = self.ids.player
        if key in [97, 100]:
            player.horizontal_speed = 0
        elif key in [119, 115]:
            player.vertical_speed = 0

class phase1(PhaseBase):
    pass

class phase2(PhaseBase):
    pass

class boneco(Image):
    base_speed = NumericProperty(1)
    horizontal_speed = NumericProperty(0)
    vertical_speed = NumericProperty(0)

class MyApp(MDApp):
    def build(self):
        Window.borderless = True

        return Builder.load_string(KV)
    def open_link(self, link):
        webbrowser.open(link)
MyApp().run()