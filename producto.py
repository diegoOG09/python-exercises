for i in range(10,101):
  value_1 = int(str(i)[0])
  value_2 = int(str(i)[1])

  doble = (value_1*value_2)*2
  if  doble == i:
    print(i)