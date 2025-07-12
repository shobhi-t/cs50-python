def main():
  phrase=input("Right, say it! ")
  playback(phrase)

def playback(phrase):
  phrase=phrase.replace(" ","...")
  print(phrase)

main()
