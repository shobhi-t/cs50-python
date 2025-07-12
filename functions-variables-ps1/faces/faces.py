def main():
  phrase=input("Right, say it! ")
  faces(phrase)

def faces(phrase):
  phrase=phrase.replace(":)","🙂").replace(":(","🙁")
  print(phrase)

main()
