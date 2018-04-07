class HangmanGame():

    def __init__(self, word):
        self.word = word.lower()
        self.counter = 6
        self.letter_list =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                         'l', 'm' ,'n' ,'o' ,'p' ,'q' ,'r', 's' ,'t' ,'u' ,'v',
                         'w' ,'x' ,'y', 'z']
        self.check_list =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                         'l', 'm' ,'n' ,'o' ,'p' ,'q' ,'r', 's' ,'t' ,'u' ,'v',
                         'w' ,'x' ,'y', 'z']

    def show_counter(self):
        print(self.counter)
    
    def create_console(self):
        self.console = []
        for letter in self.word:
            self.console.append('_')
    
    def print_console(self):
        console_string = ''
        for items in self.console:
            console_string += items +' '
        print(console_string)

    def letter_checker_length(self, letter):
        if len(letter) != 1:
            print('You can only enter one character at a time!')
            self.flag =1
        else:            
            pass
        
    def letter_checker_alpha(self,letter):
        if letter in self.check_list:
            pass
        else:
            print('Letters must be in the alphabet!')
            self.flag =1

    def letter_checker_reuse(self, letter):
        if letter not in self.letter_list:
            print('This letter has already been used!')
            self.flag =1
        else:
            pass

    def letter_checker(self, letter):
        self.flag = 0
        self.letter_checker_length(letter)
        if self.flag == 1:
            pass
        else:
            self.letter_checker_alpha(letter)
            if self.flag == 1:
                pass
            else:
                self.letter_checker_reuse(letter)

    def letter_handler(self, letter):        
        if letter in self.word:
            indices = [index for index, letters in enumerate(self.word) if letter == letters]
            for index in indices:
                self.console[index] = letter
            self.letter_list.remove(letter)
        else:
            self.letter_list.remove(letter)
            self.counter -=1

    def lost_game_end(self):
        self.show_picture()
        print('You have lost the game!')
        print('The word was: ', self.word)

    def intro_messages(self):
        print('\nThe following spaces are open: ')
        self.print_console()
        print('The following letters are available: ')
        print(self.letter_list,'\n')

    def show_picture(self):
        if self.counter == 6:
            print(' _ _ _ _')
            print('|       |')
            print('|        ')
            print('|        ')
            print('|        ')
            print('|        ')
            print('__________')
            
        elif self.counter == 5:
            print(' _ _ _ _')
            print('|       |')
            print('|       O')
            print('|        ')
            print('|        ')
            print('|        ')
            print('__________')
            
        elif self.counter == 4:
            print(' _ _ _ _')
            print('|       |')
            print('|       O')
            print('|      \ ')
            print('|        ')
            print('|        ')
            print('__________')

        elif self.counter == 3:
            print(' _ _ _ _')
            print('|       |')
            print('|       O')
            print('|      \ /')
            print('|        ')
            print('|        ')
            print('__________')

        elif self.counter == 2:
            print(' _ _ _ _')
            print('|       |')
            print('|       O')
            print('|      \ /')
            print('|       |')
            print('|        ')
            print('__________')

        elif self.counter == 1:
            print(' _ _ _ _')
            print('|       |')
            print('|       O')
            print('|      \ /')
            print('|       |')
            print('|      /')
            print('__________')
                  
        elif self.counter == 0:
            print(' _ _ _ _')
            print('|       |')
            print('|       O')
            print('|      \ /')
            print('|       |')
            print('|      / \ ')
            print('__________')
        else:
            print('Something is wrong!')      

    def game_loop(self):
        self.create_console()
        while True:
            if self.counter > 0:
                self.show_picture()
                if '_' not in self.console:
                    print('You won!')
                    print(self.console)
                    break
                else:
                    self.intro_messages()
                    letter = input('Pick your letter: ')
                    self.letter_checker(letter.lower())
                    if self.flag == 1:
                        continue
                    else:
                        self.letter_handler(letter.lower())
            else:
                self.lost_game_end()
                break
