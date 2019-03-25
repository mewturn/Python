import random
import time


def go(lower_bound, upper_bound, bots):
    iterations = 1
    target = random.randint(lower_bound, upper_bound)

    while True:
        print(f"Target number: {target}")
        answers = [random.randint(lower_bound, upper_bound)
                   for _ in range(bots)]
        scores = [answer - target for answer in answers]
        curr_low = -upper_bound
        curr_high = upper_bound
        for score in scores:
            answer = answers[scores.index(score)]

            if score == 0:
                print(
                    f"Answer found: {answers[scores.index(score)]}\nIterations required: {iterations} ")
                return answer

            if score < 0 and answer > lower_bound:
                lower_bound = answer
                print(f"Shifting lower bound to {lower_bound}")

            elif score > 0 and answer < upper_bound:
                upper_bound = answer
                print(f"Shifting upper bound to {upper_bound}")

            time.sleep(0.5)

        print(f"Searching in new range {lower_bound} to {upper_bound}")
        iterations += 1


if __name__ == "__main__":
    go(1, 100, 5)
