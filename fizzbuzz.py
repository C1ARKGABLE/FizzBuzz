'''
This is a Fizzbuzz script written in Python, based off of Tom Scott's video https://youtu.be/QPZ0pIK_wsc

Written to allow for as many words as you'd like
'''

import sys

def main(args):
  '''
  This is the main function... It just has the loop. You can add parameters if you'd like
  '''
  if len(args) == 3:

    divisors = []
    for i in args[1].split(","):
      divisors.append(int(i))

    words = []
    for i in args[2].split(","):
      words.append(i)

    for i in range(1,100):
      print(fb(i,divisors,words))
    print("divisors={0}, words={1}".format(divisors,words))

  else:

    for i in range(1,100):
      print(fb(i))
    print("divisors=[3,5], words=[\"Fizz\",\"Buzz\"]")

def fb(number, divisors=[3,5], words=["Fizz","Buzz"]):
  '''
  Takes three variables; an integer number, a list of integer divisors, and a list of words.

  If num is evenly divisible by a divisor at 'index' in divisors, the word at 'index' in words is added to the return variable. If num is not evenly divisible by any number in divisors, the original number is added as output.

  '''
  if len(divisors) != len(words):
    raise ValueError("divisors and words are not the same length but should be")

  out = ""

  for index,divisor in enumerate(divisors):

    if number % divisor == 0:
      out += words[index]

  if out == "":
    out = number

  return out

if __name__ == "__main__":
  main(sys.argv)
