import requests
import sys
import subprocess
from bs4 import BeautifulSoup
import os.path

#NEED to have part2.xsd in same folder
### CHANGE URL BELOW FOR WHATEVER PART YOU'RE ON ###
base_url = "https://cmsc420.cs.umd.edu/meeshquest/part3/input/"
base_act_input_filename = "ACT_input_"
base_act_output_filename = "ACT_output_"
base_your_output_filename = "your_output_"
i = 1

testStartNumber = 1

if len(sys.argv) != 2 and len(sys.argv) != 3:
    print "incorrect use. Pass in a .jar file and test number (optional)"
    print "sample usage: python TACT.py JARFILE.jar 4"
    print "sample usage: python TACT.py JARFILE.jar"
    exit()

if len(sys.argv) == 3:
    testStartNumber = int(sys.argv[2])

print "Downloading tests..."

ACT_input_filename = base_act_input_filename + str(i) + ".xml"
ACT_output_filename = base_act_output_filename + str(i) + ".xml"

while os.path.isfile(ACT_input_filename) and os.path.isfile(ACT_output_filename):
    i = i + 1
    ACT_input_filename = base_act_input_filename + str(i) + ".xml"
    ACT_output_filename = base_act_output_filename + str(i) + ".xml"

current_url = base_url + str(i) + "/"
page = requests.get(current_url)

while str(page.status_code) != "404":

    ACT_input_filename = base_act_input_filename + str(i) + ".xml"
    ACT_output_filename = base_act_output_filename + str(i) + ".xml"

    soup = BeautifulSoup(page.content, 'html.parser')

    test_input = soup.find('pre').get_text()
    test_output = soup.find('textarea').get_text()

    output_file = open(ACT_output_filename, 'w')
    output_file.write(test_output)
    output_file.close()

    input_file = open(ACT_input_filename, 'w')
    input_file.write(test_input)
    input_file.close()

    i = i + 1

    current_url = base_url + str(i) + "/"
    page = requests.get(current_url)

i = testStartNumber

print "Testing..."

ACT_input_filename = base_act_input_filename + str(i) + ".xml"
ACT_output_filename = base_act_output_filename + str(i) + ".xml"

while os.path.isfile(ACT_input_filename) and os.path.isfile(ACT_output_filename):
    your_output_filename = base_your_output_filename + str(i) + ".xml"
    your_output_file = open(your_output_filename, 'w')
    ACT_input_file = open(ACT_input_filename)

    process = subprocess.Popen(['java', '-jar', sys.argv[1]], stdin=ACT_input_file, stdout=your_output_file)
    process.wait()
    your_output_file.flush()
    ACT_input_file.close()
    your_output_file.close()
    
    try:
        diff = subprocess.check_output(["diff", ACT_output_filename, your_output_filename]).decode("utf-8")
        print "Test " + str(i) + " Passed " + u'\u2713'
    except subprocess.CalledProcessError as e:
        print e.output
        print "Test " + str(i) + " Failed x"

    i = i + 1
    ACT_input_filename = base_act_input_filename + str(i) + ".xml"
    ACT_output_filename = base_act_output_filename + str(i) + ".xml"
