import pygame
pygame.init()

screen={
	"width":600,
	"height":500
}
screenHeight=500

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
	"active": True
}

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


run=True
while run:
	pygame.time.delay(30)
	
	for event in pygame.event.get():
		if event.type ==pygame.QUIT:
			run=False
	
	keys=pygame.key.get_pressed()
	
	if keys[pygame.K_LEFT] and player["x"]>= player["vel"]:
		player["x"]-=player["vel"]
	if keys[pygame.K_RIGHT] and player["x"]<= screen["width"] - player["width"] - player["vel"]:
		player["x"]+=player["vel"]

	
	#player handling
	win.fill((0,0,0),pygame.Rect(0,player["y"],screen["width"],player["height"]))
	pygame.draw.rect(win,(0,0,255),(player["x"],player["y"],player["width"],player["height"]))
	
	#ball handling
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
		#check coord of platform todo
		if ball["x"] > player["x"]-ball["width"] and ball["x"]<player["x"]+player["width"]+ball["width"] :
			ball["y"]-=ball["velY"]
			ball["velY"]*=-1
			max=(ball["width"]+player["width"])
			centerBall=ball["x"]+ball["width"]/2
			centerPlayer=player["x"]+player["width"]/2
			ball["velX"]=ball["velY"]*(centerPlayer-centerBall)/(max)
	if ball["y"] >= screen["height"]:
		#lost edit it todo
		ball["y"]-=ball["velY"]
		ball["velY"]*=-1

	pygame.draw.rect(win,(255,0,0),(ball["x"],ball["y"],ball["width"],ball["height"]))

	pygame.display.update()
pygame.quit()
