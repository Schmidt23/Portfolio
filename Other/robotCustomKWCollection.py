#Collection of custom keyword functions for robot framework to handle problems encountered during writing tests

from pywinauto import Desktop
from pywinauto import keyboard
from pywinauto import Application
from robot.libraries.BuiltIn import BuiltIn
import os
import thread

def cleanup(process):
	#issues kill command to given process name. If there are multiple instances of it, all are killed
	os.system('taskkill /f /im %s' % process)

def focus_on_window(task):
	spec_dlg = Desktop(backend="uia")["%s" %task]
	spec_dlg.set_focus()
	#restore is a cheap hack to select the window
	spec_dlg.restore()

def handle_dismiss(title, dlgwd):
	# handles the alert that happens in this specific case and dismisses it. Handle is to be tailored to its specific job. TODO: Maybe more functionality
	dlg = Desktop(backend="uia")['%s' %title]
	dlg[dlgwd].set_focus()
	#dlg.restore()
	keyboard.SendKeys("{VK_ESCAPE}")
	print "handle-function finished"
  
  def press_enter():
    #press enter instead of clicking on the element because click() blocks
    spec_dlg = Desktop(backend="uia")["Login"]
    spec_dlg.set_focus()
    #restore is a cheap hack to select the window
    spec_dlg.restore()
    keyboard.SendKeys('{ENTER}')
  
def threaded_open(el, browser):
	"""Fixes the Javascript.click(). Start click() as thread to circumvent the blocking that happens when no page is immediately loaded."""
	seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
	
	def tclick(el, browser):
		seleniumlib.open_browser(el, browser)
		print "click-function finished"

    #start 1st thread with click()
	  b = thread.start_new_thread(tclick,(el,browser,))
  
def x_positions_should_be_close(xa,xb):
	#check for horizontal alignment of two elements; specifically dropdown
	if (xa - xb) < 5 and (xa-xb) >= 0 or (xa-xb) > -5 and (xa-xb) <= 0:
		print "Elements are horizontally aligned"
	else:
		raise Exception('Elements are not horizontally aligned!')
    
def start_and_expect_integrity_error(exe):
  #starts the program instead of the webdriver because of expected system-error-message which webdriver can't handle
  #requires the clean_up keyword in robot to kill when the error-message doesn't appear, because no webdriver is instantiated.
  app = Application(backend="uia").start(exe)
  #get content of error message
  error = app.Error.Static2.window_text()

  print error
  #try to close the window
  keyboard.SendKeys('{ENTER}')

  #check if the integrity is used in error message, because it's not a caught exception in the application atm
  assert "Integrit" in error, "Not Integrity Error"
