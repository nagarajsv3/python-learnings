from Question import Question
questions_prompts=[
    "What color are Apples ? \na.Purple \nb.Blue \nc.Red \n",
    "What color are Bananas ? \na.Yellow \nb.Pink \nc.Green \n",
    "What color are Strawberries ? \na.Majenta \nb.Red \nc.Blue \n"
]

questions = [
    Question(questions_prompts[0], "c"),
    Question(questions_prompts[1], "a"),
    Question(questions_prompts[2], "b")
]

def run_test(questions):
    score=0
    for question in questions:
        ans = input(question.question_prompt)
        if ans == question.answer:
            score +=1

    print("You have scored "+str(score) + " / "+str(len(questions)))

run_test(questions)