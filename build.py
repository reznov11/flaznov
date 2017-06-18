import sys
from config import Config
from modules.colors import colors
from modules.generate_app import create_app

if __name__ == "__main__":
	if len (sys.argv) != 2 :
		print '''
		 _____ _                            
		|  ___| | __ _ _____ __   _____   __
		| |_  | |/ _` |_  / '_ \ / _ \ \ / /
		|  _| | | (_| |/ /| | | | (_) \ V / 
		|_|   |_|\__,_/___|_| |_|\___/ \_/  

		Version: v0.1
		Description: Project to generate a dynamic flask application.
		Author: reznov11
		Blog: http://xakepu.blogspot.com
		Github: https://github.com/reznov11
		Twitter: @pentester11

		'''
		print colors.YELLOW + "[+] Usage: "+ colors.ENDC +"%s generate \n"%sys.argv[0]
		sys.exit (1)
	else:
		create_app(Config.APP_NAME)