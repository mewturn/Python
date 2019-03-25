import random
import time


def go(lower_bound, upper_bound, bots):
    iterations = 1
    target = random.randint(lower_bound, upper_bound)
    print(f"Target number: {'{:,}'.format(target)}")
    while True:

        answers = [random.randint(lower_bound, upper_bound)
                   for _ in range(bots)]
        scores = [answer - target for answer in answers]

        for score in scores:
            answer = answers[scores.index(score)]

            if score == 0:
                print(
                    f"Answer found: {'{:,}'.format(answer)}\nIterations required: {iterations} ")
                return answer

            if score < 0 and answer > lower_bound:
                lower_bound = answer

            elif score > 0 and answer < upper_bound:
                upper_bound = answer

        # Formatting

        print(
            f"Iteration #{iterations}: Searching in new range {'{:,}'.format(lower_bound)} to {'{:,}'.format(upper_bound)}")
        iterations += 1


if __name__ == "__main__":
    go(1, 1_000_000_000_000, 5)
