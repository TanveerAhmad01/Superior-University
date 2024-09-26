import os

class SimpleReflexAgent:
    def __init__(self, desired_temp):
        self.desired_temp = desired_temp
        self.previous_temps = self.read_previous_temps()
        self.heater_states = self.read_heater_states()

    def read_previous_temps(self):
        if os.path.exists('previous_temps.txt'):
            with open('previous_temps.txt', 'r') as f:
                temps = f.readlines()
                return {line.split(':')[0]: float(line.split(':')[1]) for line in temps}
        else:
            return {}

    def write_previous_temps(self):
        with open('previous_temps.txt', 'w') as f:
            for room, temp in self.previous_temps.items():
                f.write(f"{room}:{temp}\n")

    def read_heater_states(self):
        if os.path.exists('heater_states.txt'):
            with open('heater_states.txt', 'r') as f:
                states = f.readlines()
                return {line.split(':')[0]: line.split(':')[1].strip() for line in states}
        else:
            return {}

    def write_heater_states(self):
        with open('heater_states.txt', 'w') as f:
            for room, state in self.heater_states.items():
                f.write(f"{room}:{state}\n")

    def perceive(self, room, temp):
        self.previous_temps[room] = temp

    def act(self, room):
        if self.previous_temps[room] < self.desired_temp:
            self.heater_states[room] = "ON"
            return "TURN ON THE HEATER"
        else:
            self.heater_states[room] = "OFF"
            return "TURN OFF THE HEATER"

    def print_heater_state(self, room):
        state = self.heater_states[room]
        return f"Heater in {room} is {state}"


rooms = {
    "living room": 30,
    "kitchen": 24,
    "bedroom": 20
}

agent = SimpleReflexAgent(22)

for room, temp in rooms.items():
    agent.perceive(room, temp)
    print(f"Room: {room}, Action: {agent.act(room)}")
    print(agent.print_heater_state(room))
    agent.write_previous_temps()
    agent.write_heater_states()