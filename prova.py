import arcade

LARGHEZZA = 1200
ALTEZZA = 700
TITOLO = "Gioco di prova"

class GameView(arcade.View):

    def __init__(self):
        super().__init__()
        self.background = arcade.load_texture(
            "C:/Users/nejah.saadi/Desktop/gioco-python/immagini/sfondo.jpg"
        )
        self.personaggio = arcade.Sprite("./immagini/luffy.png")

    def on_draw(self):
        self.clear()

        # Disegna lo sfondo a schermo intero
        arcade.draw_texture_rect(self.background, arcade.LBWH(0, 0, 1200, 700))  
        arcade.draw_sprite(self.personaggio)
        

def main():
    window = arcade.Window(LARGHEZZA, ALTEZZA, TITOLO)
    view = GameView()
    window.show_view(view)
    arcade.run()

if __name__ == "__main__":
    main()
