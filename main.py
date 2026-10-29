from Pharmacy import Capsule

def main():
    aspirin = Capsule("Aspirin", 325.0, False, False)

    aspirin.print_status()
    aspirin.check_safety()
    aspirin.ckeck_alcohol_compatibility()
    aspirin.calculate_intake(75.0)
    aspirin.dissolve()

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    paracetamol = Capsule("Paracetamol", 500.0, False, True)
    paracetamol.print_status()
    paracetamol.check_safety()
    paracetamol.ckeck_alcohol_compatibility()
    paracetamol.calculate_intake(60.0)

main()
