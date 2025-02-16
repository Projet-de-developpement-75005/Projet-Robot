from Simulation import EnvRobot

class Main:
    def __init__(self):
        self.simulation = EnvRobot()

    def run(self):
        self.simulation.demarrer_simulation()

if __name__ == "__main__":
    app = Main()
    app.run()
