deck = {} #dictionary
fh = open('SYSCONFIG-D.txt').readlines()
for line in fh:
    print()
    lineList = line.decode(encoding="utf-8").split(" ")
    deduplicateSet = set(lineList)
    lineList = list(deduplicateSet)
    print(lineList)
    """ row = line.split(',')
    card_id, name, desc, hp = [i.strip() for i in row]
    card = Card(card_id, name, desc, hp)
    deck[card_id] = card #'card_id' is the 'key' and 'card' is 'value' """
