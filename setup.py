from distutils.core import setup
import py2exe
import os.path

script_dir = os.path.dirname(os.path.abspath(__file__))
setup(console=[os.path.join(script_dir,'medical_billing_calculator.py')],
      data_files = [('', [os.path.join(script_dir, "calendar-256.png")])],
	  options = {'py2exe': {
	      "optimize": 2,
		  "bundle_files": 2,
	  }},
)