print("Welcome to my question game hope you enjoy it. :)")
playing = input('Do you want to play?: ')

if playing.lower() == 'yes':
    print('welcome to my quiz game enjoy :)')

    question=input('Who is the first president of kenya?')
    if question !='kenyatta' :
        print(" you failed, The correct answer is 'kenyatta' ")
    else: print("You scored correct.")/

    question1 = input('What is the capital city of kenya?')
    if question1 != 'nairobi':
        print(" you failed, The correct answer is 'nairobi' ")
    else:
        print("You scored correct.")

        question2 = input('what is the best university in kenya')
        if question2 != 'university of nairobi':
            print(" you failed, The correct answer is 'university of nairobi' ")
        else:
            print("You scored correct.")

            question3 = input('Who owns X app?')
            if question3 != 'elon musk':
                print(" you failed, The correct answer is 'elon musk' ")
            else:
                print("You scored correct.")
else: quit()