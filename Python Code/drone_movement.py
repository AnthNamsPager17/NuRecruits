from djitellopy import Tello
from time import sleep

medical_drone = Tello()
medical_drone.connect()

print(medical_drone.get_battery())

medical_drone.takeoff()
sleep(5)
i = 0
while i < 4:
    medical_drone.send_rc_control(0, 25, 0, 90)
    sleep(2)
    i += 1

medical_drone.send_rc_control(0, 0, 0, 0)
medical_drone.land()
medical_drone.end()
