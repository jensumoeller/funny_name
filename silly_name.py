# Programm zum erzeugen von lustigen Namen
# aus zwei Listen mit Vornamen und Nachnamen,
# die zufällig miteinander kombiniert werden.

# Erste Aufgabe aus dem Buch
# "Impractical Python Projects"

import sys, random

vorName = ["Baby Oil", "Bad News", "Big Burps", "Bill 'Beenie-Weenie'", "Bob 'Stinkbug'", "Bowel Noises", "Boxelder", "Bud 'Lite'", 
	'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield', 'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread', 
	'Crab Meat', 'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso', 'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 
	'Greasy Jim', 'Huckleberry', 'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny', 'Lemongrass', 'Lil Debil', 
	'Longbranch', '"Lunch Money"', 'Mergatroid', '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch','Ovaltine', 'Pennywhistle', 
	'Pitchfork Ben', 'Potato Bug', 'Pushmeet','Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut', "Sid 'The Squirts'", 
	'Skidmark', 'Slaps', 'Snakes', 'Snoobs','Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky', 'Storyboard', 
	'Sweet Tea', 'TeeTee', 'Wheezy Joe', "Winston 'Jazz Hands'", 'Worms']

nachName = ['Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom', 'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck', 
	'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith', 'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 
	'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson', 'Kingfish', 'Listenbee', "M'Bembo", 
	'McFadden', 'Moonshine', 'Nettles', 'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf', 'Oxhandler', 
	'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow', 'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater', 
	'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern', 'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 
	'Tippins', 'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax', 'Weiners', 'Whipkey', 'Wigglesworth', 
	'Wimplesnatch', 'Winterkorn', 'Woolysocks']

for i in range(1,11):
    firstName = random.choice(vorName)
    secondName = random.choice(nachName)

    print(str(i) + ". " + firstName + " " + secondName + "\n")


