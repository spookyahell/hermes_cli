import requests
from UA import firefox

s = requests.Session()
#~ s.verify = False
r = s.get('https://www.myhermes.de/empfangen/sendungsverfolgung/sendungsinformation/', headers = firefox)
def getTrackInfo(id):
	firefox.update(
		{'content-type':'application/json',
		'Referer':'https://www.myhermes.de/empfangen/sendungsverfolgung/sendungsinformation/',
		'Accept-Language':'de,en-US;q=0.7,en;q=0.3',
		'Accept-Encoding':'gzip, deflate, br',
		'Cache-Control':'no-cache',
		'Pragma':'no-cache',
		'Connection':'keep-alive'}
		)
	r =  s.get(f'https://www.myhermes.de/services/tracking/shipments?search={id}', headers = firefox)
	if r.status_code == 204:
		return
	o = r.json()
	if 'message' in o:
		return o['message']
	else:
		return o[0]
	
if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser(
	description="Hermes Postal Package Tracker CLI"
)
	parser.add_argument('trackingid', help='trackid')
	parser.add_argument('--zusammenfassung', '-z', help='Nur die Zusammenfassung ausgeben', action = 'store_true')
	args = parser.parse_args()
	
	#~ print(args.trackingid)
	tracking = getTrackInfo(args.trackingid)
	if type(tracking) == dict:
		last = tracking['lastStatus']
		last_descr = last['description']
		last_date = last['dateTime']
		print(f'Letzter Status ({last_date}):\n{last_descr}')
		expected = tracking['expectedDate']
		if expected:
			print('Erwarteter Liefertermin:', expected)
		else:
			print('Es liegt noch kein Liefertermin vor.')
		if args.zusammenfassung or len(tracking['statusHistory']) < 2:
			exit()
		print('\n')
		statusHistory = tracking['statusHistory']
		for idx,status in enumerate(statusHistory):
			stat_descr = status['description']
			stat_date = status['dateTime']
			print(f'{idx+1}. Eintrag ({stat_date})')
			print(stat_descr)
			if idx != len(statusHistory) -1:
				print()
	elif tracking is None:
		print('ERROR: Invalid/non-existant tracking number...')
	else:
		print(f'ERROR: {tracking}')
