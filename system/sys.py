import os
import time
import winsound


def clear():

	os.system('cls')


def playsound(sound):

	winsound.PlaySound(sound, winsound.SND_ASYNC)


class ActivePhase:

	@staticmethod
	def start():
		starting_in = './sounds/active.wav'
		playsound(starting_in)

	@staticmethod
	def end():
                ending_in = './sounds/active_phase_ending_in.wav'
                playsound(ending_in)

	@staticmethod
	def active(x):
                pre_active = 5
                active_ready = x - pre_active
                ActivePhase.start()
                time.sleep(2)
                #Start.countdown()
                time.sleep(active_ready)
                #ActivePhase.end()
                #time.sleep(2)
                #Start.countdown()
                

class RestPhase:

	@staticmethod
	def start():
		starting_in = './sounds/rest.wav'
		playsound(starting_in)

	@staticmethod
	def end():
		ending_in = './sounds/rest_phase_ending_in.wav'
		playsound(ending_in)

	@staticmethod
	def rest(x):
		pre_rest = 5
		rest_ready = x - pre_rest
		RestPhase.start()
		#time.sleep(2)
		#Start.countdown()
		time.sleep(rest_ready)
		RestPhase.end()
		time.sleep(2)
		Start.countdown()


class WarmupPhase:

	@staticmethod
	def start():
		starting_in = './sounds/warmup_phase_starting_in.wav'
		playsound(starting_in)

	@staticmethod
	def end():
		ending_in = './sounds/warmup_phase_ending_in.wav'
		playsound(ending_in)

	@staticmethod
	def warmup_countdown():
                ten = './sounds/ten.wav'
                nine = './sounds/nine.wav'
                eight = './sounds/eight.wav'
                seven = './sounds/seven.wav'
                six = './sounds/six.wav'
                five = './sounds/five.wav'
                four = './sounds/four.wav'
                three = './sounds/three.wav'
                two = './sounds/two.wav'
                one = './sounds/one.wav'

                playsound(ten)
                time.sleep(1)

                playsound(nine)
                time.sleep(1)

                playsound(eight)
                time.sleep(1)

                playsound(seven)
                time.sleep(1)

                playsound(six)
                time.sleep(1)

                playsound(five)
                time.sleep(1)

                playsound(four)
                time.sleep(1)

                playsound(three)
                time.sleep(1)

                playsound(two)
                time.sleep(1)

                playsound(one)
                time.sleep(1)
                

	@staticmethod
	def warmup(x):
		pre_warmup = 5
		warmup_ready = x - pre_warmup
		WarmupPhase.start()
		time.sleep(2)
		Start.countdown()
		time.sleep(warmup_ready)
		WarmupPhase.end()
		time.sleep(2)
		WarmupPhase.warmup_countdown()


class CooldownPhase:

	@staticmethod
	def start():
		starting_in = './sounds/cooldown_phase_starting_in.wav'
		playsound(starting_in)

	@staticmethod
	def end():
		ending_in = './sounds/cooldown_phase_ending_in.wav'
		playsound(ending_in)

	@staticmethod
	def cooldown(x):
		pre_cooldown = 5
		cooldown_ready = x - pre_cooldown
		CooldownPhase.start()
		time.sleep(2)
		Start.countdown()
		time.sleep(cooldown_ready)
		CooldownPhase.end()
		time.sleep(2)
		Start.countdown()


class Success:

        @staticmethod
        def goodjob():
                job_complete = ''

class Beep:

	@staticmethod
	def single():
		freq = 2500
		dur = 1000
		winsound.Beep(freq, dur)

	@staticmethod
	def multi():
		freq = 2500
		dur = 1000
		for s in range(1, 5):
			winsound.Beep(freq, dur)


class Start:

	def exercises(x, y, z, zz):
		total_set = x * y
		for r in range(total_set):
                        ActivePhase.active(z)
                        RestPhase.rest(zz)


	@staticmethod
	def countdown():
		three = './sounds/three.wav'
		two = './sounds/two.wav'
		one = './sounds/one.wav'

		playsound(three)
		time.sleep(1)

		playsound(two)
		time.sleep(1)

		playsound(one)
		time.sleep(1)

