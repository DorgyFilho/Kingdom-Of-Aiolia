import random
import time

Win = None
YouHP = 100
CpuHP = 100

def Intro():
    print()
    print('''December 31, 2099
The world is at its intellectual peak. Today, humanity is experiencing its greatest period of prosperity, 
as the advances made throughout the twenty-first century have allowed people to live in absolute peace. 
However, a tyrant coming from the Middle Ages opened a portal to spread the wickedness and destruction in our world. 
To avoid such a tragedy, the Kingdom of Aiolia resorted to a warrior from the human world who had all the 
characteristics necessary to face Wolfgang and save the world. Who will win the battle?''')
    print('\n')
    
    time.sleep(5)

    print('''Messenger: You were the chosen one to defeat the tyrant Wolfgang von Spectrum. You gather all the 
characteristics of a great warrior into a battle of such importance. Our warriors tried to stop him, but perished 
before this monster that wants to cause pain and suffering for the people. Win Wolfgang and you will be remembered 
as a legendary warrior, forever.''')
    print()

    time.sleep(5)


def Battle(): #Battle System

    global Win, YouHP, CpuHP

    play = True

    while play:

        Win = None
        YouHP = 100
        CpuHP = 100

        turn = random.randint(1,2)

        if turn == 1:
            You = True
            Cpu = False
            print('Your Turn')
            print()
        
        else:
            You = False
            Cpu = True
            print("Cpu's Turn")
            print()
        
        print('You: {} HP\nCpu: {} HP'.format(YouHP, CpuHP))
        print()
        
        while YouHP !=  0 or CpuHP != 0:
            Immune = False
            Cure = False

            #Moves' Dictionary
            moves = {'PUNCH':random.randint(10,25), 
            'SLASH':random.randint(15,25),
            'TORNADO':random.randint(14,35),
            'CURE':random.randint(15,30)}

            #Your Turn
            if You:
                print()
                print('1-PUNCH\n2-SLASH\n3-TORNADO\n4-CURE')
                print()
                pMove = input('Answer: ').upper()
                print()

                Immune = random.randint(1,3)

                if Immune == 1:
                    Immune = True
                else:
                    Immune = False
                
                if Immune:
                    pMove = 0
                    print()
                    print('You Miss')
                    print()
                
                else: #You Move
                    if pMove in ('1', 'PUNCH'):
                        pMove = moves['PUNCH']
                        print()
                        print("You inflicted {} damage to Opponent's HP".format(pMove))
                        print()
                    elif pMove in ('2', 'SLASH'):
                        pMove = moves['SLASH']
                        print()
                        print("You inflicted {} damage to Opponent's HP".format(pMove))
                        print()
                    elif pMove in ('3', 'TORNADO'):
                        pMove = moves['TORNADO']
                        print()
                        print("You inflicted {} damage to Opponent's HP".format(pMove))
                    elif pMove in ('4', 'CURE'):
                        Cure = True
                        pMove = moves['CURE']
                        print()
                        print('You Healed {} HP'.format(pMove))
                    else:
                        print()
                        print('Invalid Option!')
                        print()
                        continue
            
            #CPU Moves
            else:
                #No Damage.
                Immune = random.randint(1,3)

                if Immune == 1:
                    Immune = True
                else:
                    Immune = False
                
                if Immune:
                    cMove = 0
                    print()
                    print('Computer Miss')
                    print()
                
                #Battle
                else:
                    if CpuHP > 55:
                        if YouHP >= 70:
                            cMove = moves['PUNCH']
                            print()
                            print('Cpu inflicted {} damage to your HP.'.format(cMove))
                            print()
                        elif 30 < YouHP < 70:
                            cMove = moves['SLASH']
                            print()
                            print('Cpu inflicted {} damage to your HP.'.format(cMove))
                            print()
                        elif YouHP <= 30:
                            cMove = moves['TORNADO']
                            print()
                            print('Cpu inflicted {} damage to your HP.'.format(cMove))
                            print()
                    
                    #Cure Or Battle?
                    else: #Cure
                        CureOrBattle = random.randint(1,2)
                        if CureOrBattle == 1:
                            Cure = True
                            cMove = moves['CURE']
                            print()
                            print('Cpu healed {} HP.'.format(cMove))
                            print()
                        
                        #Battle
                        else:
                            if YouHP >= 70:
                                cMove = moves['PUNCH']
                                print()
                                print('Cpu inflicted {} damage to your HP.'.format(cMove))
                                print()
                            elif 30 < YouHP < 70:
                                cMove = moves['SLASH']
                                print()
                                print('Cpu inflicted {} damage to your HP.'.format(cMove))
                                print()
                            elif YouHP <= 30:
                                cMove = moves['TORNADO']
                                print()
                                print('Cpu inflicted {} damage to your HP'.format(cMove))
                                print()
            
            #You Cure
            if Cure:
                if You:
                    YouHP += pMove
                    if YouHP > 100: #Overtake the maximum HP
                        YouHP = 100 #Maximum HP
                
                #Cpu's Cure
                else:
                    CpuHP += cMove
                    if CpuHP > 100: #Overtake the maximum HP
                        CpuHP = 100 #Maximum HP
            
            #Battle
            else:
                if You: #You Win
                    CpuHP -= pMove
                    if CpuHP < 0 or CpuHP == 0:
                        CpuHP = 0
                        Win = 'You'
                        break
                
                else: #Cpu Wins
                    if Cpu:
                        YouHP -= cMove
                        if YouHP < 0 or YouHP == 0:
                            YouHP = 0
                            Win = 'Cpu'
                            break

            #Status
            print('You: {} HP\nCpu: {} HP'.format(YouHP, CpuHP))
            print()

            #Random 'won't work' because this part is responsible for alternate turns.
            You = not You
            Cpu = not Cpu
        
        if (Win == 'You' and CpuHP == 0) or (Win == 'Cpu' and YouHP == 0):
            print()
            print('End Of Battle.')
            print()
            time.sleep(2)
            break

#Final Result
def Result():
    Battle()
    if Win == 'You' and CpuHP == 0:
        print()
        print('Status\nYou: {} HP\nCpu: {} HP\nYou Win!'.format(YouHP, CpuHP))
        print()
        print('''You got what seemed impossible to us. You defeated the tyrant Wolfgang von Spectrum! 
    Thanks to you, the human world can live in peace in every age. You are the legendary warrior of the 
    Kingdom of Aiolia. We will always remember your heroic act. Thank you!''')
        print()
        time.sleep(5)

        #You Lose!!!
    else:
        print()
        print('Status\nYou: {} HP\nCpu: {} HP\nYou Lose!'.format(YouHP, CpuHP))
        print()
        print('''Messenger: Unfortunately you succumbed to Wolfgang. Now the world is lost.''')
        print()
        time.sleep(5)

#MAIN MENU
def mainMenu():
    again = 'Y'
    while again == 'Y':
        print('{:50}'.format('KINGDOM OF AIOLIA'))
        print()
        print('S-Start\nQ-Quit')
        print()
        op = input('Press the option: ').upper()
        if op == 'S':
            Intro()
            Result()
        elif op == 'Q':
            print('Shutdown!')
            exit()
        else:
            print('Invalid Option,')
            print()
        
        print('Do You Want to Try Again? Y or N')
        print()
        again = input('Select Your Option: ').upper()
        if again == 'N':
            print('Shutdown!')
            exit()
    else:
        print('Invalid Option!')
        exit()

mainMenu()


