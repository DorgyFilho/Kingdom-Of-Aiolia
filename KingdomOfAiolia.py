import random
import time

def intro():
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

def finalBattle():

    play = True

    while play: #While the game is working...
        Win = None
        YouHP = 100
        CpuHP = 100

        turn = random.randint(1,2) #Players' Turn
        
        #Your Turn
        if turn == 1:
            You = True
            Cpu = False
            print('Your Turn')

        
        #CPU's Turn
        else:
            You = False
            Cpu = True
            print("Cpu's Turn")
        
        #Status
        print('You: {} HP\nCpu: {} HP'.format(YouHP, CpuHP))
        print()
        
        #Battling...
        while YouHP != 0 or CpuHP != 0:
            Immune = False
            Cure = False

            #Moves' Dictionary
            moves = {'PUNCH': random.randint(10,25),
            'SLASH': random.randint(15, 25),
            'TORNADO': random.randint(14, 35),
            'CURE': random.randint(15,30)}
            
            #Your Turn. Select Your Move.
            if You:
                print('1-PUNCH\n2-SLASH\n3-TORNADO\n4-CURE')
                print()
                pMove = input('Answer: ').upper()
                print()

                Immune = random.randint(1,3)

                if Immune == 1:
                    Immune = True
                else:
                    Immune = False
                
                #No Damage Inflicted
                if Immune:
                    pMove = 0
                    print()
                    print('You Miss')
                    print()
            
                else: #Moves.
                    if pMove in ('1', 'PUNCH'):
                        pMove = moves['PUNCH']
                        print('You inflicted {} damage'.format(pMove))
                        print()
                    elif pMove in ('2', 'SLASH'):
                        pMove = moves['SLASH']
                        print('You inflicted {} damage'.format(pMove))
                        print()
                    elif pMove in ('3', 'TORNADO'):
                        pMove = moves['TORNADO']
                        print('You inflicted {} damage'.format(pMove))
                    elif pMove in ('4', 'CURE'):
                        Cure = True
                        pMove = moves['CURE']
                        print('You healed {} HP'.format(pMove))
                        print()
                    else:
                        print('Invalid Move!')
                        print()
                        continue

            #Cpu will select your turn.
            else:
                Immune = random.randint(1,3)

                if Immune == 1:
                    Immune = True
                else:
                    Immune = False
                
                #No Damage Inflicted
                if Immune:
                    cMove = 0
                    print()
                    print('Computer Miss')
                    print()
                
                #Cpu's Move.
                else:
                    if CpuHP > 55:
                        if YouHP >= 70:
                            cMove = moves['PUNCH']
                            print()
                            print('Cpu inflicted {} damage HP!'.format(cMove))
                            print()
                        elif 30 < YouHP < 70:
                            cMove = moves['SLASH']
                            print()
                            print('Cpu inflicted {} damage HP!'.format(cMove))
                            print()
                        elif YouHP <= 30:
                            print()
                            print('Cpu inflicted {} damage HP!'.format(cMove))
                            print()
                        

                    else:
                        CureOrFight = random.randint(1,2)
                        if CureOrFight == 1:
                            Cure = True
                            cMove = moves['CURE']
                            print()
                            print('CPU healed {} HP'.format(cMove))
                            print()
                        else:
                            if YouHP >= 70:
                                cMove = moves['PUNCH']
                                print()
                                print('Cpu inflicted {} damage HP!'.format(cMove))
                                print()
                            elif 30 < YouHP < 70:
                                cMove = moves['SLASH']
                                print()
                                print('Cpu inflicted {} damage HP!'.format(cMove))
                                print()
                            elif YouHP <= 30:
                                cMove = moves['TORNADO']
                                print()
                                print('Cpu inflicted {} damage HP'.format(cMove))
                                print()
            #You's Cure
            if Cure:
                if You:
                    YouHP += pMove
                    if YouHP > 100: #Overtake the HP limit.
                        YouHP = 100 #Start HP.
                #Cpu's Cure
                else:
                    CpuHP += cMove
                    if CpuHP > 100:
                        CpuHP = 100
            #Battle!
            else:
                #You Win!
                if You:
                    CpuHP -= pMove
                    if CpuHP < 0 or CpuHP == 0:
                        CpuHP = 0
                        Win = 'You'
                        break
                else:
                    #You Lose!
                    YouHP -= cMove
                    if YouHP < 0 or YouHP == 0:
                        YouHP = 0
                        Win = 'Cpu'
                        break

            
            print('STATUS')
            print()
            print('You: {} HP\nCpu: {} HP'.format(YouHP, CpuHP))
            print()

            #Random "won't work" because this part is responsible for alternate turns.
            You = not You
            Cpu = not Cpu

        #You Win!!!
        if Win == 'You' and (CpuHP == 0 or CpuHP < 0):
            print('Status\nYou: {} HP\nCpu: {} HP\nYou Win!'.format(YouHP, CpuHP))
            print()
            print('''You got what seemed impossible to us. You defeated the tyrant Wolfgang von Spectrum! 
        Thanks to you, the human world can live in peace in every age. You are the legendary warrior of the 
        Kingdom of Aiolia. We will always remember your heroic act. Thank you!''')
            time.sleep(5)
            break
        #You Lose!!!
        else:
            print()
            print('Status\nYou: {} HP\nCpu: {} HP\nYou Lose!'.format(YouHP, CpuHP))
            print('''Messenger: Unfortunately you succumbed to Wolfgang. Now the world is lost.''')
            print()
            time.sleep(5)
            break

def main():
    again = 'Y'
    while again == 'Y':
        print()
        print('{:50}'.format('KINGDOM OF AIOLIA'))
        print()
        print('S-Start\nQ-Quit')
        print()
        op = input('Answer: ').upper()
        print()
        if op == 'S':
            intro()
            finalBattle()
        elif op == 'Q':
            print('Shutdown')
            exit()
        else:
            print('Invalid Option!')

        print()
        print('Do You Want To Try Again? Y or N')
        print()
        again = input('Option: ').upper()
        if again == 'N':
            print('Shutdown!')
            exit()
    else:
        print('Invalid Option')
        exit()

main()



