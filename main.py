from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
from enigma_simulator.enigma import Enigma

def datetime_now():
    print(datetime.now(tz=None))

def enigma():
    # Encrypting
    enigma1 = Enigma(["I", "II", "III"], [1, 1, 1], "B", "AD", [0, 0, 0])
    enigma1.encrypt("HELLOXWORLD")  # Returns "LOFUHZZLZOB"

    # Decrypting
    enigma2 = Enigma(["I", "II", "III"], [1, 1, 1], "B", "AD", [0, 0, 0])
    enigma2.encrypt("LOFUHZZLZOB")  # Returns "HELLOXWORLD" back
    print(enigma1)
    print(enigma2)

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    datetime_now()
    enigma()
