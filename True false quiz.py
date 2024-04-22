class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_number = 1

    def ask_question(self, question, answer):
        print("Q.",self.question_number)
        print(question)
        user_answer = input("True or False? (Enter 'T' for True, 'F' for False): ").strip().upper()
        if (user_answer == 'T' and answer) or (user_answer == 'F' and not answer):
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect! The correct answer is:", answer)
        self.question_number += 1

    def play(self):
        print("Welcome to the Indian History True or False Quiz!")
        #print("You'll be asked 30 questions. Let's get started!\n")
        for question, answer in self.questions.items():
            self.ask_question(question, answer)
        print("\nQuiz complete!")
        print("Your final score is:", self.score)
        if self.score >= 25:
            print("Congratulations! You passed the quiz!")
            return True
        else:
            retry = input("Sorry, you did not pass the quiz. Would you like to try again? (yes/no): ").strip().lower()
            if retry == "yes":
                return False
            else:
                print("Thank you for playing!")
                return True


# Define your questions dictionary here
questions_dict = {
    "The Indian National Congress was founded in 1857.": False,
    "The first war of Indian independence took place in 1857.": True,
    "Mahatma Gandhi was born in 1870.": False,
    "The Indian constitution was adopted on January 26, 1950.": True,
    "The capital of India before New Delhi was Kolkata.": True,
    "The Jallianwala Bagh massacre occurred in 1919.": True,
    "The Taj Mahal was built by Shah Jahan.": True,
    "The Indian state of Goa was liberated from Portuguese rule in 1961.": True,
    "The Battle of Plassey was fought in 1757.": True,
    "The Indian National Army (INA) was founded by Subhas Chandra Bose.": True,
    "Indira Gandhi was the first female Prime Minister of India.": False,
    "The Quit India Movement was launched in 1942.": True,
    "The partition of India and Pakistan occurred in 1947.": True,
    "The Dandi March was led by Jawaharlal Nehru.": False,
    "The Indian currency symbol '₹' was adopted in 2010.": True,
    "The first Mughal emperor of India was Babur.": True,
    "The Indian state of Kerala is known as the 'Land of Spices'.": True,
    "The Ashoka Chakra has 24 spokes.": True,
    "Rani Lakshmi Bai of Jhansi was a prominent leader during the Indian Rebellion of 1857.": True,
    "The Indian city of Mumbai was formerly known as Bombay.": True,
    "The Battle of Buxar took place in 1764.": True,
    "The term 'Swaraj' was popularized by Mahatma Gandhi.": True,
    "The Red Fort in Delhi was built by Emperor Akbar.": False,
    "The Indian state of Punjab is known for the Golden Temple.": True,
    "The Suez Canal Crisis of 1956 involved India, Egypt, and the UK.": True,
    "The Maratha Empire was founded by Shivaji Maharaj.": True,
    "The Indus Valley Civilization is one of the oldest civilizations in the world.": True,
    "The Indian national anthem 'Jana Gana Mana' was written by Rabindranath Tagore.": True,
    "The Battle of Panipat in 1526 marked the beginning of Mughal rule in India.": True,
    "The Indian state of Bihar is known for the ancient university of Nalanda.": True,
}

# Create an instance of the QuizGame class and start playing
while True:
    quiz = QuizGame(questions_dict)
    if quiz.play():
        break