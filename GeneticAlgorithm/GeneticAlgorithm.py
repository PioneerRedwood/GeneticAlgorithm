import random as rand
import math, copy


class GeneticAlgorithm:

    def __init__(self, num_iterations, num_offsprings, num_chromosomes):
        self.num_iterations = num_iterations
        self.num_offsprings = num_offsprings
        self.num_chromosomes = num_chromosomes

        # 2차원 배열
        self.population = self.initialize_population()

    def perform_evolution(self):

        for gen in range(self.num_iterations):

            # 1차원 배열
            offsprings = [0 for i in range(self.num_offsprings)]

            # 개발자가 지정하는 교배 및 변이 횟수
            num_crossover = math.ceil(self.num_offsprings / 2) + rand.randint(0, 2)
            num_mutation = math.ceil(self.num_offsprings / 9)

            crossover = 0
            mutation = 0
            maintain = 0

            for idx in range(self.num_offsprings):
                case = 0
                # 부모 선택
                p1, p2 = self.select_parents(self.population)

                # 교배
                if num_crossover >= 0 & idx < self.num_offsprings - 1:
                    offsprings[idx], offsprings[idx + 1] = self.crossover_parents(p1, p2)
                    num_crossover -= 1
                    crossover += 1
                    case = 1

                # 변이
                if num_mutation >= 0:
                    offsprings[idx] = self.mutation(offsprings[idx], idx)
                    num_mutation -= 1
                    mutation += 1
                    case = 2

                # 유지
                if case == 0:
                    offsprings[idx] = self.population[idx]
                    maintain += 1

            self.population = self.substitute_population(offsprings)
            print("#", gen, "th population\n", self.population, "\ncrossover: ", crossover, " mutation: ", mutation,
                  "maintain: ", maintain, "\n")

        most_fittest = self.find_best_solution()

        print("The best offspring in the history")
        return self.population[most_fittest]

    # Initialize population generation: Requires solution encoding
    # 첫 세대 정보 초기화
    def initialize_population(self):
        population = []

        for i in range(self.num_offsprings):
            arr = []
            for j in range(self.num_chromosomes):
                arr.append(rand.randint(0, 1))
            population.append(arr)

        return population

    # Selection of two solutions to be used for making a new solution
    # 부모를 선택, 두 크로모섬을 반환
    def select_parents(self, population):
        sum = [0 for i in range(self.num_offsprings)]

        for itr in range(self.num_offsprings):
            for itr2 in range(self.num_chromosomes):
                sum[itr] += self.population[itr][itr2]

        sorted_sum = copy.deepcopy(sum)
        sorted_sum.sort(reverse=True)

        return self.population[sum.index(sorted_sum[0])], self.population[sum.index(sorted_sum[1])]

    # Creating a new solution from the selected solutions
    # 두 부모에 의해 새로운 자식 반환
    def crossover_parents(self, p1, p2):
        pivot = math.ceil(self.num_chromosomes / 2)
        new1 = p1[:pivot] + p2[pivot:]
        new2 = p1[pivot:] + p2[:pivot]

        return new1, new2

    # Introducing some changes in the new solution
    # 변이 적용, 일정 수만큼 변이 적용
    def mutation(self, offspring, idx):
        temp = copy.deepcopy(offspring)

        # 짝수면 반전
        if idx % 2 == 0:
            num = rand.randint(0, self.num_chromosomes - 1)
            if temp[num] == 0:
                temp[num] = 1
            else:
                temp[num] = 0
        # 홀수면 교체
        else:
            pivot = math.ceil(self.num_chromosomes / 2)
            num1 = rand.randint(0, pivot)
            num2 = rand.randint(pivot, self.num_chromosomes - 1)

            temp[num1] = temp[num2]
            temp[num2] = temp[num1]

        return temp

    # Replace the new solution in the population
    # 기존 유전자 대체
    # noinspection PyMethodMayBeStatic
    def substitute_population(self, offsprings):
        next_gen = copy.deepcopy(offsprings)
        return next_gen

    # 가장 적절한 솔루션 반환
    def find_best_solution(self):
        sum = []
        max = 0

        for itr in self.population:
            a = 0
            for itr2 in itr:
                a += itr2
            sum.append(a)
            if a > max:
                max = a

        idx = sum.index(max)
        return idx


def main():
    # GeneticAlgorithm(num_iteration, num_offsprings, num_chromosomes)
    ga = GeneticAlgorithm(6, 10, 10)
    print(ga.perform_evolution())


if __name__ == "__main__":
    main()
