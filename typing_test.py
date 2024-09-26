import time
import random

def typing_test():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a versatile programming language.",
        "Practice makes perfect when it comes to typing.",
        "Coding is both an art and a science.",
        "Efficiency is key in software development."
    ]

    print("Welcome to the Typing Test!")
    print("Type the following sentence as quickly and accurately as you can.")
    print("Press Enter when you're done.")
    
    sentence = random.choice(sentences)
    print("\n" + sentence + "\n")
    difficulty_levels = {
        "easy": [
            "The quick brown fox jumps over the lazy dog. This simple sentence contains every letter of the alphabet. It has been used for years to test typewriters and computer keyboards. The sentence is also used in handwriting practice and to display font samples.",
            "Python is a versatile programming language. It was created by Guido van Rossum and released in 1991. Python is known for its simplicity and readability. It is widely used in web development, data analysis, artificial intelligence, and scientific computing.",
            "Cats are fascinating creatures. They sleep for up to 16 hours a day, which is why they're often seen napping in sunny spots. Cats have excellent night vision and can hear sounds at higher frequencies than humans or even dogs. They use their whiskers to gauge whether they can fit through small spaces."
        ],
        "medium": [
            "Practice makes perfect when it comes to typing. The more you type, the faster and more accurate you become. It's important to focus on accuracy first, then gradually increase your speed. Many people find that using online typing games or software can help improve their skills. Remember to take breaks to avoid strain on your hands and wrists.",
            "Coding is both an art and a science. It requires logical thinking and problem-solving skills, but also creativity and intuition. Good programmers not only write functional code but also strive for elegance and efficiency. Learning to code can be challenging, but it's also incredibly rewarding. As technology continues to advance, coding skills become increasingly valuable in many industries.",
            "The early bird catches the worm, but the second mouse gets the cheese. This proverb highlights the balance between being proactive and being cautious. While it's often advantageous to be first, sometimes it's better to learn from others' mistakes. In life and in business, timing can be crucial. It's important to assess situations carefully and decide when to act quickly and when to wait for the right moment."
        ],
        "hard": [
            "Efficiency is key in software development. As applications grow in complexity, optimizing code becomes increasingly important. This involves not only writing faster algorithms but also considering factors like memory usage, scalability, and maintainability. Profiling tools can help identify bottlenecks in your code. It's also crucial to balance efficiency with readability and simplicity. Sometimes, a slightly less efficient solution might be preferred if it's significantly easier to understand and maintain.",
            "The quick brown fox jumps over the lazy dog and runs circles around it. This sentence, known as a pangram, contains every letter of the English alphabet. It's often used by graphic designers to display typefaces. The fox's agility contrasts with the dog's laziness, creating a vivid mental image. This simple sentence has been a staple in typing tests and font demonstrations for decades, showcasing its versatility and memorability in various contexts.",
            "In the depths of winter, I finally learned that there was in me an invincible summer. This quote by Albert Camus speaks to the resilience of the human spirit. It suggests that even in our darkest moments, we have an inner strength that can help us persevere. The metaphor of winter representing hardship and summer representing hope is powerful and universally relatable. This quote reminds us that challenges are temporary and that we have the capacity to overcome them."
        ],
        "legend": [
            "Arvind - Efficiency is key in software development. As applications grow in complexity, optimizing code becomes increasingly important. This involves not only writing faster algorithms but also considering factors like memory usage, scalability, and maintainability. Profiling tools can help identify bottlenecks in your code. It's also crucial to balance efficiency with readability and simplicity. Sometimes, a slightly less efficient solution might be preferred if it's significantly easier to understand and maintain.            The quick brown fox jumps over the lazy dog and runs circles around it. This sentence, known as a pangram, contains every letter of the English alphabet. It's often used by graphic designers to display typefaces. The fox's agility contrasts with the dog's laziness, creating a vivid mental image. This simple sentence has been a staple in typing tests and font demonstrations for decades, showcasing its versatility and memorability in various contexts.            In the depths of winter, I finally learned that there was in me an invincible summer. This quote by Albert Camus speaks to the resilience of the human spirit. It suggests that even in our darkest moments, we have an inner strength that can help us persevere. The metaphor of winter representing hardship and summer representing hope is powerful and universally relatable. This quote reminds us that challenges are temporary and that we have the capacity to overcome them."
        ]
    }

    print("Select difficulty level: easy, medium, hard, legend")
    difficulty = input().strip().lower()

    while difficulty not in difficulty_levels:
        print("Invalid choice. Please select again: easy, medium, hard")
        difficulty = input().strip().lower()

    sentence = random.choice(difficulty_levels[difficulty])
    print("\n" + sentence + "\n")

    input("Press Enter when you're ready to start...")
    
    start_time = time.time()
    user_input = input()
    end_time = time.time()

    time_taken = end_time - start_time
    words = len(sentence.split())
    characters = len(sentence)
    
    accuracy = calculate_accuracy(sentence, user_input)
    wpm = calculate_wpm(words, time_taken)

    print(f"\nTime taken: {time_taken:.2f} seconds")
    print(f"Words per minute: {wpm:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")

def calculate_accuracy(original, typed):
    if len(typed) == 0:
        return 0.0
    correct_chars = sum(1 for a, b in zip(original, typed) if a == b)
    return (correct_chars / len(original)) * 100

def calculate_wpm(words, time_taken):
    minutes = time_taken / 60
    return words / minutes

if __name__ == "__main__":
    typing_test()
