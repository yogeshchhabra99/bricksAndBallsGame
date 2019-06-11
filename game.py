import pygame
import numpy as np
import math

pygame.init()

screen={
	"width":600,
	"height":500
}
screenHeight=500

white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 

win = pygame.display.set_mode((screen["width"],screen["height"]))

pygame.display.set_caption("Ball Game")

player={
	"x" : 0,
	"y" : 0,
	"width" : 70,
	"height" : 20,
	"vel" : 8
}
player["y"] = screen["height"]-player["height"]

brick={
	"width":60,
	"height":25,
	"color":(0,255,0),
}

class Brick:
	def __init__(self, x,y):
		self.x=x
		self.y=y
		

ball={
	"x":screen["width"]/2,
	"y":screen["height"]/2,
	"width":20,
	"height":20,
	"velX":0,
	"velY":-10
}
ball["x"]-=ball["width"]/2
ball["y"]-=ball["height"]/2

#Text
font = pygame.font.Font('freesansbold.ttf', 32) 

gameOverText = font.render('Game Over', True, green, blue) 
gameOverTextRect = gameOverText.get_rect()  
gameOverTextRect.center = (screen["width"] // 2, screen["height"] // 2 -100) 


score=0
time=0

#3 lists of bricks
list1=[]
list2=[]
list3=[]

gapMax=15
margin=6
height1 = math.floor(1.2*margin+np.random.rand()*gapMax);
height2 = height1 + math.floor(1.2*margin+np.random.rand()*gapMax)+brick["height"];
height3 = height2 + math.floor(1.2*margin+np.random.rand()*gapMax)+brick["height"];

x=math.floor(margin+np.random.rand()*gapMax)
while x+brick["width"] < screen["width"]:
	list1.append(Brick(x,height1))
	x+=math.floor(margin+np.random.rand()*gapMax)
	x+=brick["width"]

x=math.floor(margin+np.random.rand()*gapMax)
while x+brick["width"] < screen["width"]:
	list2.append(Brick(x,height2))
	x+=math.floor(margin+np.random.rand()*gapMax)
	x+=brick["width"]
	
x=math.floor(margin+np.random.rand()*gapMax)
while x+brick["width"] < screen["width"]:
	list3.append(Brick(x,height3))
	x+=math.floor(margin+np.random.rand()*gapMax)
	x+=brick["width"]


run=True
gameOver=False
pause=False
won=False

def getScore():
	return math.floor(score*10-time/30)
while run:
	
	if (not gameOver) and (not won): 
		time=time+1;
	pygame.time.delay(30)
	
		

	
	for event in pygame.event.get():
		if event.type ==pygame.QUIT:
			run=False
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_p:
				if pause:
					pause=False
				else:
					pause=True	
			if event.key==pygame.K_s:
				list1=[]
				list2=[]
				list3=[]	

	if pause:
		continue	
	
	if gameOver:
		win.fill((0,0,0))
		win.blit(gameOverText,gameOverTextRect)
		
		scoreText = font.render('Score: '+str(getScore()), True, green, blue) 
		scoreTextRect = scoreText.get_rect()  
		scoreTextRect.center = (screen["width"] // 2, screen["height"] // 2+100) 

		win.blit(scoreText,scoreTextRect)		

		pygame.display.update()
		continue
	

	if (not list1) and (not list2) and (not list3) :
		won=True
	if won:
		win.fill((0,0,0))
		scoreText = font.render('You Win, Score: '+str(getScore()), True, green, blue) 
		scoreTextRect = scoreText.get_rect()  
		scoreTextRect.center = (screen["width"] // 2, screen["height"] // 2) 

		win.blit(scoreText,scoreTextRect)		
		pygame.display.update()
		continue
	
	keys=pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and player["x"]>= player["vel"]:
		player["x"]-=player["vel"]
	if keys[pygame.K_RIGHT] and player["x"]<= screen["width"] - player["width"] - player["vel"]:
		player["x"]+=player["vel"]
	
	#score Printing
	text = font.render('Score: '+str(getScore()), True, green, blue) 
	textRect = text.get_rect()  
	textRect.center = (screen["width"] // 2, screen["height"] // 2) 
	#win.fill((0,0,0),pygame.textRect.x)
	win.blit(text,textRect)	

	
	#bricks drawing
	for var in list1:
		pygame.draw.rect(win,brick["color"],(var.x,var.y,brick["width"],brick["height"]))
	for var in list2:
		pygame.draw.rect(win,brick["color"],(var.x,var.y,brick["width"],brick["height"]))
	for var in list3:
		pygame.draw.rect(win,brick["color"],(var.x,var.y,brick["width"],brick["height"]))
	
	#player drawing
	win.fill((0,0,0),pygame.Rect(0,player["y"],screen["width"],player["height"]))
	pygame.draw.rect(win,(0,0,255),(player["x"],player["y"],player["width"],player["height"]))
	
	#ball drawing
	win.fill((0,0,0),pygame.Rect(ball["x"],ball["y"],ball["width"],ball["height"]))
	ball["x"]+=ball["velX"]
	ball["y"]+=ball["velY"]

	if ball["x"] <=	-ball["width"]/2:
		ball["x"]-=ball["velX"]
		ball["velX"]*=-1
	elif ball["x"] >= screen["width"]-ball["width"]-ball["velX"]:
		ball["x"]+=ball["velX"]
		ball["velX"]*=-1
	elif ball["y"] <= -ball["height"]:
		ball["y"]-=ball["velY"]
		ball["velY"]*=-1
	elif ball["y"] >= screen["height"]-player["height"] -ball["velY"]:
		if ball["x"] > player["x"]-ball["width"] and ball["x"]<player["x"]+player["width"]+ball["width"] :
			ball["y"]-=ball["velY"]
			ball["velY"]*=-1
			max=(ball["width"]+player["width"])
			centerBall=ball["x"]+ball["width"]/2
			centerPlayer=player["x"]+player["width"]/2
			ball["velX"]=ball["velY"]*(centerPlayer-centerBall)/(max)
	if ball["y"] >= screen["height"]:
		gameOver=True

	pygame.draw.rect(win,(255,0,0),(ball["x"],ball["y"],ball["width"],ball["height"]))

	pygame.display.update()

	
	#handle colision
	col=False
	if ball["y"] > height1-ball["height"] and ball["y"] < height1+brick["height"] :
		for var in list1:
			if ball["x"] > var.x-ball["width"] and ball["x"]<var.x+brick["width"] :
				list1.remove(var)
				#paint black too
				win.fill((0,0,0),pygame.Rect(var.x ,var.y,brick["width"],brick["height"]))
				col=True

		if col:
			#ball["velX"]*=-1
			ball["velY"]*=-1
			score=score+1
			continue
	if ball["y"] > height2-ball["height"] and ball["y"] < height2+brick["height"] :
		for var in list2:
			if ball["x"] > var.x-ball["width"] and ball["x"]<var.x+brick["width"] :
				list2.remove(var)
				win.fill((0,0,0),pygame.Rect(var.x ,var.y,brick["width"],brick["height"]))
				col=True

		if col:
			#ball["velX"]*=-1
			ball["velY"]*=-1
			score=score+1
			continue
	
	if ball["y"] > height3-ball["height"] and ball["y"] < height3+brick["height"] :
		for var in list3:
			if ball["x"] > var.x-ball["width"] and ball["x"]<var.x+brick["width"] :
				list3.remove(var)
				win.fill((0,0,0),pygame.Rect(var.x ,var.y,brick["width"],brick["height"]))
				col=True

		if col:
			#ball["velX"]*=-1
			ball["velY"]*=-1
			score=score+1
			continue
	
		
			
pygame.quit()
