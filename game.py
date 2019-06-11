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
	"vel" : 7
}
player["y"] = screen["height"]-player["height"]

run=True
while run:
	pygame.time.delay(40)
	
	for event in pygame.event.get():
		if event.type ==pygame.QUIT:
			run=False
	
	keys=pygame.key.get_pressed()
	
	if keys[pygame.K_LEFT] and player["x"]> player["vel"]:
		player["x"]-=player["vel"]
	if keys[pygame.K_RIGHT] and player["x"]< screen["width"] - player["width"] - player["vel"]:
		player["x"]+=player["vel"]
	if keys[pygame.K_UP] and player["y"]>vel:
		player["y"]-=player["vel"]
	if keys[pygame.K_DOWN] and player["y"]< screen["height"] - player["height"] - player["vel"]:
		player["y"]+=player["vel"]


	win.fill((0,0,0))
	pygame.draw.rect(win,(0,0,255),(player["x"],player["y"],player["width"],player["height"]))
	pygame.display.update()
pygame.quit()
