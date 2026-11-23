if keys[pygame.K_LEFT]:
    player_x -= 5
if keys[pygame.K_RIGHT]:
    player_x += 5
if keys[pygame.K_UP]:
    player_y -= 5
if keys[pygame.K_DOWN]:
    player_y += 5

if player_x > width - 40:
    player_x = width - 40
elif player_x < 0:
    player_x = 0


if player_y > height - 40:
    player_y = height - 40
elif player_y < 0:
    player_y = 0

timer += 1
if timer % 60 == 0:
    speed += 0.03

    while len(enemies) < 2:
        img = enemy1 if random.randint(0,1)==0 else enemy2
        enemies.append([random.randint(0,width-40),0,img])

    player_rect = pygame.Rect(player_x,player_y,40,40)
    screen.blit(player_img, (player_x,player_y))
