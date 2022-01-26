class Player :
    def __init__(self,pseudo,score0,score1,score2,score3,score4,highestscore,lowestscore) :
        self.__score1 = score1
        self.__score2 = score2
        self.__score3 = score3
        self.__score4 = score4
        self.__score0 = score0
        self.__pseudo= pseudo
        self.__highest=highestscore
        self.__lowest= lowestscore
    def getScore0(self,score0) :
       self.__score0 += score0
       return self.__score0
    def getScore1(self,score1) :
        self.__score1 += score1
        return self.__score1
    def getScore2(self,score2) :
       self.__score2 += score2
       return self.__score2
    def getScore3(self,score3) :
       self.__score3 += score3
       return self.__score3
    def getScore4(self,score4) :
        self.__score4 += score4
        return self.__score4
    def getPseudo (self) :
       return self.__pseudo
    def getHighscore (self,highestscore,score0,score1,score2,score3,score4) :
       if score0 > score1 and score0 > score2 and score0 > score3 and score0 > score4 :
           highestscore = score0
           self.__highest += highestscore
       elif score1 > score0 and score1 > score2 and score1 > score3 and score1 > score4 :
           highestscore = score1
           self.__highest += highestscore
       elif score2 > score0 and score2 > score1 and score2 > score3 and score2 > score4 :
           highestscore = score2
           self.__highest += highestscore
       elif score3 > score0 and score3 > score1 and score3 > score2 and score3 > score4 :
           highestscore = score3
           self.__highest += highestscore
       elif score4 > score0 and score4 > score1 and score4 > score3 and score4 > score2 :
           highestscore = score4
           self.__highest += highestscore
       return self.__highest
    def getLowscore (self,lowestscore,score0,score1,score2,score3,score4) :
         if score0 < score1 and score0 < score2 and score0 < score3 and score0 < score4 :
           lowestscore = score0
           self.__lowest += lowestscore
         elif score1 < score0 and score1 < score2 and score1 < score3 and score1 < score4 :
           lowestscore = score1
           self.__highest += lowestscore
         elif score2 < score0 and score2 < score1 and score2 < score3 and score2 < score4 :
           lowestscore = score2
           self.__highest += lowestscore
         elif score3 < score0 and score3 < score1 and score3 < score2 and score3 < score4 :
           lowestscore = score3
           self.__highest += lowestscore
         elif score4 < score0 and score4 < score1 and score4 < score3 and score4 < score2 :
           lowestscore = score4
           self.__lowest +=score4
         return self.__lowest


class Karaoké : 
    def __init__(self,playernumber,deleteplayer,playernames) :

joueur1= Player("Gloubox",0,0,0,0,0,0,0)
lyric1= ["o","f","h"]
lyric2= ["b","p","h"]
quit = False
while quit == False :

    choixdechanson = int(input("Quelle chanson voulez vous essayez ? (répondez par des chiffre de 1 à 5) "))
    if choixdechanson == 1 :
        print("Les paroles de la chanson vont s'afficher...")
        print(lyric1[0],lyric1[1],lyric1[2])
        playerrespond = [input(" (écrivez chaque lettre une par une) "),input(""),input("")]
        if playerrespond[0] == lyric1[0] and playerrespond[1] == lyric1[1] and playerrespond[2] == lyric1[2] :
            print ("Bravo, vous avez le score maximum")
            joueur1 = Player("Gloubox",100,0,0,0,0,0,0)
        elif playerrespond[0] != lyric1[0] and playerrespond[1] == lyric1[1] and playerrespond[2] == lyric1[2] :
            print("Bravo, vous avez fini la chanson.")
            joueur1 =Player("Gloubox",80,0,0,0,0,0,0)
        elif playerrespond[0] == lyric1[0] and playerrespond[1] != lyric1[1] and playerrespond[2] == lyric1[2] :
            print("Bravo, vous avez fini la chanson.")
            joueur1 =Player("Gloubox",80,0,0,0,0,0,0)
        elif playerrespond[0] == lyric1[0] and playerrespond[1] == lyric1[1] and playerrespond[2] != lyric1[2] :
            print("Bravo, vous avez fini la chanson.")
            joueur1 =Player("Gloubox",80,0,0,0,0,0,0)
        elif playerrespond[0] != lyric1[0] and playerrespond[1] != lyric1[1] and playerrespond[2] == lyric1[2] :
            print("Bravo, vous avez fini la chanson.")
            joueur1 =Player("Gloubox",60,0,0,0,0,0,0)
        elif playerrespond[0] != lyric1[0] and playerrespond[1] == lyric1[1] and playerrespond[2] != lyric1[2] :
            print("Bravo, vous avez fini la chanson.")
            joueur1 =Player("Gloubox",60,0,0,0,0,0,0)
        elif playerrespond[0] == lyric1[0] and playerrespond[1] != lyric1[1] and playerrespond[2] != lyric1[2] :
            print("Bravo, vous avez fini la chanson.")
            joueur1 =Player("Gloubox",60,0,0,0,0,0,0)
        elif playerrespond[0] != lyric1[0] and playerrespond[1] != lyric1[1] and playerrespond[2] != lyric1[2] :
            print("Bravo, vous avez fini la chanson.")
            joueur1 =Player("Gloubox",50,0,0,0,0,0,0)
    if choixdechanson == 2 :
        print("Les paroles de la chanson vont s'afficher...")
        print(lyric2[0],lyric2[1],lyric2[2])
        playerrespond = [input(" (écrivez chaque lettre une par une) "),input(""),input("")]
        if playerrespond[0] == lyric2[0] and playerrespond[1] == lyric2[1] and playerrespond[2] == lyric2[2] :
            print ("Bravo, vous avez le score maximum")
            joueur1 = Player("Gloubox",100,0,0,0,0,0,0)
        elif playerrespond[0] != lyric2[0] and playerrespond[1] == lyric2[1] and playerrespond[2] == lyric2[2] :
            print("Bravo, vous avez fini la chanson.")
            joueur1 =Player("Gloubox",80,0,0,0,0,0,0)
        elif playerrespond[0] == lyric1[0] and playerrespond[1] != lyric1[1] and playerrespond[2] == lyric1[2] :
            print("Bravo, vous avez fini la chanson.")
            joueur1 =Player("Gloubox",80,0,0,0,0,0,0)
        elif playerrespond[0] == lyric1[0] and playerrespond[1] == lyric1[1] and playerrespond[2] != lyric1[2] :
            print("Bravo, vous avez fini la chanson.")
            joueur1 =Player("Gloubox",80,0,0,0,0,0,0)
        elif playerrespond[0] != lyric1[0] and playerrespond[1] != lyric1[1] and playerrespond[2] == lyric1[2] :
            print("Bravo, vous avez fini la chanson.")
            joueur1 =Player("Gloubox",60,0,0,0,0,0,0)
        elif playerrespond[0] != lyric1[0] and playerrespond[1] == lyric1[1] and playerrespond[2] != lyric1[2] :
            print("Bravo, vous avez fini la chanson.")
            joueur1 =Player("Gloubox",60,0,0,0,0,0,0)
        elif playerrespond[0] == lyric1[0] and playerrespond[1] != lyric1[1] and playerrespond[2] != lyric1[2] :
            print("Bravo, vous avez fini la chanson.")
            joueur1 =getattr(Player, __score0 : 60)
        elif playerrespond[0] != lyric1[0] and playerrespond[1] != lyric1[1] and playerrespond[2] != lyric1[2] :
            print("Bravo, vous avez fini la chanson.")
            joueur1 = getattr(Player, __score0 : 50 )