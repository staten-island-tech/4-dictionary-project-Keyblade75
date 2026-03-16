def gamble(quarters,m1,m2,m3):
        plays=0
        one=35-m1
        two=100-m2
        three=10-m3
        stage=1
        while quarters != 0:
                quarters-=1
                plays +=1
                if stage == 1:
                        one += 1
                        stage ==2
                        if one == 35:
                                quarters += 29
                                one == 0
                                if quarters == 0:
                                       if stage == 2: 
                                        two += 1
                        stage == 3
                        if two == 100:
                                quarters += 59
                        two == 0
                if stage == 3:
                       three += 1 
                       if three == 10:
                        quarters += 9 and three == 0
                        stage == 1
                if quarters == 0:
                      print(plays)
                      break
gamble(48,3,10,4)