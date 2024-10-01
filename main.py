import random

#Funktion som avgör vem som får poäng eller om det är oavgjort
#Funktionen returnerar 0 för oavgjort, -1 för poäng för datorn och 1 för poäng för männinska
def calculateWinner():
   
    if computer_choice_str == human_choice:
        return 0
    else:
        if computer_choice_str=="sten":
            if human_choice=="sax":
               return -1
            else:
               return 1

        if computer_choice_str=="sax":
            if human_choice=="påse":
               return -1
            else:
               return 1

        if computer_choice_str=="påse":
            if human_choice=="sten":
               return -1
            else:
               return 1
    # Slutar funktionen

#Funktion som testar om det inmatade värdet är ett giltigt värde
#Returnerar ordet som versaler
def testinput():
    input_counter = 0
    while input_counter < 5:
            try:
                human_input = input("Ange ditt värde: ")
                valid_answers = ['sten', 'sax', 'påse']
                if human_input.lower() not in valid_answers:
                    input_counter += 1  
                    if input_counter > 3:
                        return "Error"
                    else:
                        raise ValueError('Inte giltigt värde. Du måste ange sten eller sax eller påse.')
                else:
                    return human_input.lower()
            except ValueError as err:
                print(err)


#Klass där varje instans representerar en spelomgång för att spara val och resultat
class gameRound:
    def __init__(self, gameNo, humanInput, humanScore, comupterInput, computerScore):
        self.gameNo = gameNo
        self.humanInput = humanInput
        self.humanScore = humanScore
        self.comupterInput = comupterInput
        self.computerScore = computerScore
    
    def __str__(self):
        return f"Runda {self.gameNo} du {self.humanInput} datorn {self.comupterInput}"   


# ============ Start ==============

#Initiering
choiceNum_dict1 = { "1":"sten", "2":"sax", "3":"påse" }
maxNoRounds = 20
limit_for_victory = 3

human_totalscore = 0
computer_totalscore = 0

game_list = []
keep_playing = True

print("Så trevligt att du vill spela sten - sax - påse")
print("Först till tre poäng vinner! \n")


# Start spel loop
count = 1
while keep_playing:
    print(f"Runda: {count}")
    input_Counter = 0
    human_choice = testinput()

    if human_choice=="Error":
        print("Spelet avslutas eftersom du inte anger ett korrekt värde")
        break
     
    computer_choice_int = random.randint(1,3)
    computer_choice_str = choiceNum_dict1[str(computer_choice_int)]
    print(f"{human_choice} (du) - {computer_choice_str}  (datorn)" ) 
 
 # Avgör resultatet av omgången och delar ut poäng
    if calculateWinner()==-0:
        print("Oavgjort")
        computer_score = 0
        human_score = 0
    elif calculateWinner()==-1:
        print("Datorn vann omgången")
        computer_score = 1
        human_score = 0
        computer_totalscore += 1
    elif calculateWinner()==1:
        print("Du vann omgången")
        computer_score = 0
        human_score = 1
        human_totalscore += 1
    else:
        print("Något gick fel. Kan inte avggöra resultatet för omgången. Avslutar spelet")
        keep_playing = False  #break   # Bryter ur loopen

#Skapar en instans av classen
    gameRoundLoad = gameRound(count, human_choice, human_score, computer_choice_str, computer_score)
#Lägger till instansen i spellistan
    game_list.append(gameRoundLoad)

    print(f"Din totalpoäng: {human_totalscore} Datorns totalpoäng: {computer_totalscore} \n")
    count += 1 

# Testar ifall spelet ska avslutas
    if (human_totalscore >= int(limit_for_victory) ):
        print("Grattis du vann! Spelet slut.")
        print("Runda: Ditt val (poäng) | Datorns val (poäng)")
        for gameRoundLoad in game_list:
            print(f"{gameRoundLoad.gameNo} : {gameRoundLoad.humanInput} ({gameRoundLoad.humanScore}) | {gameRoundLoad.comupterInput} ({gameRoundLoad.computerScore})")
        keep_playing = False  #break  
        
    elif (computer_totalscore >= int(limit_for_victory) ):
        print("Tyvärr datorn vann! Spelet slut")
        print("Runda: Ditt val (poäng) | Datorns val (poäng)")
        for gameRoundLoad in game_list:
            print(f"{gameRoundLoad.gameNo} : {gameRoundLoad.humanInput} ({gameRoundLoad.humanScore}) | {gameRoundLoad.comupterInput} ({gameRoundLoad.computerScore})")
        keep_playing = False  #break   
       
    elif (count >= maxNoRounds):
        print("Nu är jag trött och avslutar spelet")
        keep_playing = False  #break   
    
    #Slut spel loop
