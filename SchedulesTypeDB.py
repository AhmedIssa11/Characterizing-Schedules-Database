import shutil
tSize = shutil.get_terminal_size().columns

sched = input('Please Enter The Schedule : ')
print('-'*80)
def cleanDate(sched):
    sched = sched.replace(" ","")
    sched = sched.replace(")","")
    sched = sched.replace("(","")
    sched = sched.lower()
    sched = sched.split(";")
    sched.remove('')
    return sched


def schedType(readFlag,writeFlag,commitFirstFlag):
    if readFlag == False and writeFlag == False and commitFirstFlag == True:
        return "Strict"
    elif readFlag == False and writeFlag == True and (commitFirstFlag == True or commitFirstFlag == False):
        return 'Cascadeless'
    elif readFlag == True and (writeFlag == True or writeFlag == False) and commitFirstFlag == True:
        return 'Recoverable'
    elif readFlag == True and writeFlag == True and commitFirstFlag == False:
        return "Non Recoverable"
    
    
readFlag,writeFlag,commitFirstFlag = False,False,False
sched = cleanDate(sched)
print(' '.join(sched).center(tSize))
print('-'*80)

''' Catch the First Write'''
for row in sched:
#    print(row)
    if 'w' in row:
        schedNum = row[1]
        schedRes = row[2]
        pos = sched.index(row) + 1
        break
    
#print(schedNum,schedRes,pos,sep=' ')
for i in range(pos,len(sched)):
    
    if sched[i][0] == 'w' and sched[i][1] != schedNum and sched[i][2] == schedRes:
        writeFlag = True
        
    if sched[i][0] == 'r' and sched[i][1] != schedNum and sched[i][2] == schedRes:
        readFlag = True
        
    if sched[i][0] == 'c':
        if sched[i][1] == schedNum:
            commitFirstFlag = True
        else:
            commitFirstFlag = False
        break
        
print(' '* 15,"Read: " + str(readFlag),
      "Write: " + str(writeFlag),
      "Commit First: " + str(commitFirstFlag),
      sep = '   ')

print('-'*80)

Stype = '**** ' + schedType(readFlag,writeFlag,commitFirstFlag) + ' ****'
print(Stype.center(tSize))
    
    