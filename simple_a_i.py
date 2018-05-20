import random
import os

class Memory:
    def __init__(self, action, reaction):
        self.action = action
        self.reaction = reaction


class SimpleAI:

    def __init__(self):
        self.brain_filename = "brain.txt"
        self.memories = []
        if os.path.isfile(self.brain_filename):
            with open(self.brain_filename, 'r') as brain_file:
                for line in brain_file.readlines():
                    line_split = line.split()
                    if 2 != len(line_split):
                        print "Line Error: " + line
                        continue
                    else:
                        self.memories.append(Memory(line_split[0], line_split[1]))

    def __del__(self):
        with open(self.brain_filename, 'w') as brain_file:
            for memory in self.memories:
                brain_file.write(repr(memory.action) + " " + memory.reaction + "\n")

    def action(self):
        if len(self.memories):
            for memory in self.memories:
                if "good" == memory.reaction:
                    return memory.action
        return random.randint(0,2)

    def saveReaction(self, action, reaction):
        self.memories.insert(0, Memory(action, reaction))

def main():
    bot = SimpleAI()

    while True:
        action = bot.action()
        print "Action: " + repr(action)
        reaction = raw_input('Reaction: ')
        if 'quit' == reaction:
            break
        bot.saveReaction(action, reaction)


if __name__ == "__main__":
    main()

