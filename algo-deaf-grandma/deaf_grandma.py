def deaf_grandma():
    exit = False
    previous_goodbye = False
    
    print('You have engaged into a conversation with your granny.')
    print('You can just stop talking and walk away by saying, "I\'m out!"\n')
    
    while(exit == False):
        talk = input('Say something to granny: ')
       
        if talk == "":
            print('WHAT?!')
        elif talk.lower() == "i'm out!" or talk.lower() == "i'm out":
            exit = True
        elif talk == 'GOODBYE!':
            if previous_goodbye:
                print('LATER, SKATER!')
                break                
            else:
                previous_goodbye = True
                print('LEAVING SO SOON?')
        elif talk.isupper():
            print('NO, NOT SINCE 1946!')
        else:
            print('SPEAK UP, KID!')

deaf_grandma()