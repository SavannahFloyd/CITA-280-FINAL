import time
def timer(timerSeconds):
    timer = timerSeconds
    print (timer)
    time.sleep(1)
    for i in range(timer):
        timer = timer - 1
        print(timer)
        time.sleep(1)
        ## if playerSprite gets a time boost:
        ##      timer = timer + 5
        if timer == 0: ##or player health == 0:
            print("GAME OVER")
        ## elif player reaches end and timer > 0:
            ## print("YOU WIN!")
