
colorlist1 = set((input('Enter the colors for list1 : ')).split(','))

colorlist2 = set((input('Enter the colors list2 : ')).split(','))

print('Colors present in color-list1 not contained in color-list2 are: ',list(colorlist1.difference(colorlist2)))