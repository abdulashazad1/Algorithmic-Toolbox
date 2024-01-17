def change(money):
    # greedy algo that takes highest possible first
    # and then the rest is auto completed with denominations 1,5,10
    coins = 0
    while money >= 10:
        money -= 10
        coins += 1
    while money >= 5:
        money -= 5
        coins += 1
    while money >= 1:
        money -= 1
        coins += 1
    
    return coins


if __name__ == '__main__':
    m = int(input())
    print(change(m))
