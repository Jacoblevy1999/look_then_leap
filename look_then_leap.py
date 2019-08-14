import random

class SecretaryProblem(object):

    def __init__(self, max_number, candidates):
        self.numbers = self.make_array(max_number, candidates)
        self.chosen = None
        self.maxPos = self.numbers.index(max(self.numbers))

    def make_array(self, max_number, candidates):
        arr = []
        for number in range(0, candidates):
            arr.append(random.randint(0, max_number))
        return arr

    def choose_number(self, pos):
        self.chosen = self.numbers[pos]


class Simulation(object):

    def __init__(self, times_to_simulate, number_of_cadidates, max_number):
        self.times = times_to_simulate
        self.candidates = number_of_cadidates
        self.max_number = max_number

    def simulate(self):
        success = []
        for i in range(0, self.candidates):
            successes_at_pos = 0
            for e in range(0, self.times):
                problem = SecretaryProblem(self.max_number, self.candidates)
                curr_max = 0
                return_pos = self.candidates
                for j in range(0, self.candidates):
                    if j < i:
                        if problem.numbers[j] > curr_max:
                            curr_max = problem.numbers[j]
                    elif j >= i:
                        if problem.numbers[j] >= curr_max:
                            return_pos = j
                            break
                if return_pos == problem.maxPos:
                    successes_at_pos += 1
            success_rate = float(successes_at_pos/e)*100

            success.append(success_rate)
        return success

