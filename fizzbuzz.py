'''
This is a Fizzbuzz script written in Python, based off of Tom Scott's video https://youtu.be/QPZ0pIK_wsc

Written to allow for as many words as you'd like
'''

def main():
  '''
  This is the main function... It just has the loop. You can add parameters if you'd like
  '''
  for i in range(1,100):
    print(fb(i))


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
  main()
