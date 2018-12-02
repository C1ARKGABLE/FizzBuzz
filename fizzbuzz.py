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


def fb(num, ls=[3,5], words=["Fizz","Buzz"]):
  '''
  Takes three variables; an integer number (num), a list of integer divisors (ls), and a list of words (words).

  If num is evenly divisible by a divisor at 'index' in ls, the word at 'index' in words is added to the return variable. If num is not evenly divisible by any number in ls, the original number is added as output.

  '''
  if len(ls) != len(words):
    raise ValueError("ls and words are not the same length but should be")


  out = ""
  for index,item in enumerate(ls):
    if num % item == 0:
      out += words[index]
  if out == "":
    out = num
  return out

if __name__ == "__main__":
  main()
