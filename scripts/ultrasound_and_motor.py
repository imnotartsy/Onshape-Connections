import hub,utime
from spike import DistanceSensor
from spike.control import wait_for_seconds
distance_sensor = DistanceSensor('A')
while True:
	last_distance = distance_sensor.get_distance_cm()
	wait_for_seconds(1)
	new_distance = distance_sensor.get_distance_cm()
	while last_distance != new_distance:
	    hub.port.C.motor.run_at_speed(speed = new_distance, max_power = 100, acceleration = 100, deceleration = 100, stall = False)

	