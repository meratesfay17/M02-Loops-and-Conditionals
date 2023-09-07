secret = 7  # You can choose any number between 1 and 10 as the secret number
guess = 4   # You can choose any number between 1 and 10 as the guess

if guess < secret:
    print('too low')
elif guess > secret:
    print('too high')
else:
    print('just right')
