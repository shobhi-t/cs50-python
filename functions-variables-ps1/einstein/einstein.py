def main():
  mass=int(input("m: "))
  mass_to_energy(mass)

def mass_to_energy(mass):
  energy=mass*300000000*300000000
  print("E:", energy)

main()
