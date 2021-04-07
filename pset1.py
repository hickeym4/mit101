primenumcount = 2
testnum = 2
while primenumcount <=1000:
    testnum = testnum + 1
    denom = testnum-1
    stopindicator = 0
    while stopindicator <1:
        while denom > 1:
            if testnum % denom == 0:
                stopindicator = 1
            if denom == 2 and stopindicator ==0:
                primenumcount = primenumcount+1
                stopindicator = 1
            else:
                denom = denom-1






print("The 1000th prime number is:")
print(testnum)



#