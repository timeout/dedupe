class App:
    def __init__(self):
        print("ctor")

    def run(self):
        print("Well, hello there...")

def main() -> None:
    app = App()
    app.run()
