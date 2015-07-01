#!/usr/bin/python
num = int( raw_input( "Enter a number: " ) )
for i in range(1, (num/2)+1):
  if num%i == 0:
    print str(i) + ' x ' + str(num/i)