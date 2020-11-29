import random, copy

from flask import Flask, render_template, request

 

app = Flask(__name__)

 

questions = {

    "Q. Having _____ about your suggestion for a few days, I've decided to support the project." : [ " (a) thinking" , "(b) thought ", "(c) think ", "(d) to think" ," (b) thought "  ] ,

    "Q. He's been working there ______ ten years." : [  " (a) for ", "(b) since ", "(c) already ", "(d) till" ,"(a) for" ] ,

    " Q. Nothing happened at the meeting, _____ it? " : [  "(a) didnt" , "(b) do ", "(c) does ", "(d) did " , "(d) did " ] ,

    " Q. It's about time we ________ , it's nearly midnight.": [ "(a) leave", "(b) left" , "(c) to leave ", "(d) leaving ", "(b) left  " ] ,

    " Q. The house will ______ at the end of the year." : [  " (a) be sell" , "(b) sold ", "(c) be sold ", "(d) selling ", "(c) be sold "]  ,

    " Q. Did you remember ______ the parcels? " : [" (a) to post" , "(b)posting ", "(c) post" , "(d) for posting" , "(a) to post"] ,

    " Q. Can you tell me when ________ leaving?"  : [ "(a) does the plane" , "(b) is the plane ", "(c) the plane is" , "(d) the plane ", "(c) the plane is " ] ,

    " Q. I must get ________ - I cant use the internet at all." : [  " (a) my computer fixed" , "(b) my computer's fix ", "(c) fixed my computer" , "(d) my computer fix", "(a) my computer fixed  " ] ,

    " Q. I dont know if I can do it but I will ______ a go." : [  " (a) make ", "(b) give ", "(c) see ", "(d)have ", "(d)have  " ] ,

    " Q. I can't find my keys ________ ." : [  " (a) anywhere" , "(b) everywhere ", "(c) anything ", "(d) any place", "(a) anywhere " ] ,

    " Q. People ______ the Earth was flat until Aristotle ______ that it was not." : [  " (a)believed / was proving ", "(b) had believed / proved  ", "(c)had believed / would prove  ", "(d) have believed / proved ", "(b) had believed / proved " ] ,

    " Q. Ever since I stopped working, I ________ to save money by ________ at home." : [  " (a)have tried / having being cooked ", "(b) tried / cooking ", "(c)have tried / cook ", "(d)have been trying / cooking" , "(d)have been trying / cooking  " ] ,

    " Q. My girlfriend and I ______ to find the right agent who ______ us find the perfect home." : [  " (a) had tried / has help" , "(b) were trying / will help ", "(c) have been trying / will help " , "(d) are trying / will have helped ", "(c) have been trying / will help " ] ,

    " Q. He ________ the one who crashed your car yesterday, he was with me the whole time." : [  " (a) may have been" , "(b) can't have been  ", "(c) may not have been ", "(d) shouldn't have been ", "(b) can't have been  " ] ,

    " Q. Computer records ______ that they ________ us before the product was shipped." : [   "(a)  showed / had paid " , "(b) has shown / have paid ", "(c) had shown / will pay ", "(d) showed / would be paid ","(a)  showed / had paid " ] ,

    " Q. Every time we go there, we take a lot of pictures ________ we take a drive along the beach to see the surfers.": [ " (a) so that " , "(b) as ", "(c) whereas"  , "(d) lest ", "(b) as " ] ,

    " Q. All inclusive resorts are best for families with kids, ________ unmarried couples." : [  " (a) as well as ", "(b) so as to ", "(c) consequently" , "(d) thereby " , "(a) as well as" ] ,

    " Q. Andriy Shevchenko, _____ goals I have watched over and over, was a legendary soccer player." : [  " (a) which " , "(b) where ", "(c) whose ", "(d) who ", "(c) whose " ],

    " Q. This is the place _____ James inadvertently had his first kiss." : [  " (a) which ", "(b) whose ", "(c) where" , "(d) that ", "(c) where "  ],

    " Q. It is very distracting if the students chatter around while the teacher ________." : [  " (a) would lecture" , "(b) were lecturing ", "(c) will lecture ", "(d) is lecturing ", "(d) is lecturing " ] ,

    " Q. I bought myself a new set of tools ______ I am going to build a new home for Puffy." : [  " (a) which ", "(b) when ", "(c) with which" , "(d) in which ", "(c) with which " ] ,

    " Q. Aristotle was among those ______ tried to prove the Earth was actually spherical and not flat." : [  " (a) whose" , "(b) to whom ", "(c) where ", "(d) who ", "(d) who " ] ,

    " Q. Those are the kind of movies ______ many Americans would rate as mature." : [  "(a) which " , "(b) where ", "(c) in which" , "(d) of which"," (a) which " ],

    " Q. There are known to be total of eight planets in the Solar System ______ is the Earth." : [  " (a) which ", "(b) that ", "(c) through which" , "(d) one of which " , "(d) one of which " ] ,

    " Q. Eclipse is the event ______ tonight in North America.": [  " (a) that observed " , "(b) which are observing  ", "(c) being observed" , "(d) having observed ", "(c) being observed "] ,

    " Q. I don't like ______ by a cop car ________ I am driving alone because it makes me nervous." : [  " (a) being followed / while ", "(b) being followed / where ", "(c) to follow / while ", "(d) to be followed / that", "(a) being followed / while " ] ,

    " Q. ______ I decided not to have a carrier in English, I still want to learn it." : [  " (a) Despite" , "(b) Although ", "(c) Due to" , "(d) Therefore" , "(b) Although " ] ,

    " Q. She suddenly wants to get married, ______ moving out and finding a job in Michigan." : [  " (a) while ", "(b) moreover ", "(c) in addition to" , "(d) in contrast  ", "(c) Due to"],

    " Q. The teacher advised us to go to every class and turn in our homework assignments timely ______ happens." : [" (a) due to the fact that" , "(b) no matter what ", "(c) accordingly ", "(d) however  " ,"(b) no matter what " ] ,

    " Q. My parents are finally going to get ______ a car so I won't have to drive them around anymore." : [" (a) on their own ", "(b) themselves ", "(c) theirs " , "(d) they  ","(b) themselves " ] ,

    " Q. Don't worry, by the time you ______ home I ______ dinner. ": ["(a) came / will make" , "(b) have come / would have made ", "(c) come / will have made" , "(d) had come / made" , "(b) themselves " ] ,

    " Q. My father ______ to help out in the house since my mother started working.": [" (a) had tried" , "(b) tried ", "(c) was trying" , "(d) has been trying  ","(d) has been trying  " ] ,

    " Q. ____ having the best player in the league, we lost 3 games in a row.": [ " (a) due to" , "(b) in spite of the fact that ", "(c) as ", "(d) despite  " ,"(d) despite  " ] ,

    " Q. I can't remember very well but I ______ your friend at the bazaar.": [ " (a) may have met" , "(b) shouldn't have met ", "(c) should have met ", "(d) should meet  ", " (a) may have met" ] ,

    " Q. The company hired so many new employees last week, ______ they laid off two workers whose performance hadn't been satisfactory.": [" (a) in addition to" , "(b) as a result of this ", "(c) on the other hand ", "(d) consequently  ", "(c) on the other hand "] ,

    " Q. Public schools in the city ______ be free, now half of the people cannot afford them.": [" (a) are used to" , "(b) used to ", "(c) use to ", "(d) using to  ",  "(b) used to "],

    " Q. The stand up show we went to see yesterday, ______ made my day, lasted only one hour.": [" (a) that" , "(b) who ", "(c) whom" , "(d) which  ","(d) which  "] ,

    " Q. Daniel was exhausted ______ all day playing in the backyard.": [" (a) spending ", "(b) having spent ", "(c)spent" , "(d) being spent  ", "(b) having spent "  ] ,

    " Q. The dealership has very fancy cars in their inventory, most ______ are very expensive." : [ " (a) that ", "(b) which ", "(c) of which" , "(d) of whose  " ,"(c) of which" ] ,

    " Q. My roommate complained about all the bugs ______ around since we moved in." : [ " (a) having been flying ", "(b) to be flying ", "(c) have flown ", "(d) to being flown  " ," (a) having been flying " ] ,

    " Q. All of these houses, ______ are falling apart already, will be put down.": [ "(a) which ", "(b) what ", "(c) that ", "(d) for which  ","(a) which " ] ,

    " Q. My cousin shared his lunch with me, ______ was very kind of him." :[ " (a) where" , "(b) that ", "(c) who ", "(d) which  " ,"(d) which  "] ,

    " Q. My English teacher is going to join us for lunch, ______ father is the principle of the school." : [" (a) which" , "(b) whose ", "(c) that ", "(d) what  " ,"(b) whose " ] ,

    " Q. He drove instead of flying ______ he could stop by his uncle on the way there.": [ " (a) so that ", "(b) in case ", "(c) hence" , "(d) however  "," (a) so that " ],

    " Q. We lost our final game and ______ we didn't make it to the top 16.": [ " (a) therefore" , "(b) notwithstanding ", "(c) however" , "(d) since  " ," (a) therefore" ] ,

    " Q. It doesn't mean she loves you just ______ she accepted to go to the movies with you.": [ " (a) due to ", "(b) despite ", "(c) yet" , "(d) because  ", "(d) because  "] ,

    " Q. Angelina has been the girl of your dreams, ______?": [ " (a) hasn't she" , "(b) isn't it ", "(c) doesn't she" , "(d) did she  " , " (a) hasn't she"] ,

    " Q. When he ______ from the company he ______ for 20 years, he felt devastated." : [ " (a) has been fired / has worked ", "(b) was fired / had been working ", "(c) fired / had worked ", "(d) fired / worked  " ,"(b) was fired / had been working " ] ,

    " Q. By the time I ______ enough money, it ______ too late to turn things around." : [ " (a) save / has been ", "(b) had saved / has been ", "(c) had saved / was ", "(d) have saved / was " , "(d) have saved / was "] ,

    " Q. _____ the French Revolution, many citizens had become upset with the aristocracy." : [ "(a) By the time" , "(b) Until", "(c) By the time of " , "(d) Till" , "(c) By the time of " ]

    }   

 

 

@app.route('/')

def grammar():

    for (question , opt) in random.sample(questions.items(), k =10) :

        print (question,opt[:4])

        

    return render_template('grammar.html', r = random.sample(questions.items(),k=10))

 

@app.route('/grammar', methods = ['POST'])

def grammar_answers() :

    score = 0

    for opt in random.sample(questions.items(),k =10):

        answer = request.form

        if opt[1][4]== answer :

            score = score+1

    print(score)

    return '<h1> Score : '+ str(score)+'</h1>'

 

 

  

#calling main function 

if __name__=="__main__":

    app.run(debug=True)
 
