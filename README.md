# TACT
Tester for MeeshQuest's Automated Canonical Tester

### Overview

This short python script first goes through all of the existing tests on the ACT and downloads all of the tests you currently don't have.
The script then runs your jar file with all of the tests, and uses diff to compare the ACT output and your jar file's output.
The python script will be timeconsuming running the first time, as it has to download all of the tests. I ran the script fresh against 2500 tests for part 2, and it took several minutes.

### Prerequisites

Have a Linux machine (not sure if this works for Windows because the script uses diff)

Have Python 2.7 (not sure if this works for Python 3)

Set up [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

### Installing

1) Create a new folder, and place TACT.py into new folder

2) Create a runnable JAR file.

* In Eclipse, Right click your project, choose 'Export...'
* In the pop-up, underneath Java, choose 'Runnable JAR file' and click Next
* In Launch Configuration dropdown, choose 'MeeshQuest - PROJECT_NAME_YOU_ARE_EXPORTING'
* Make the export destination the same folder TACT.py is in and click Finish

3) Place the relevant part_.xsd file in the same folder as TACT.py

4) In the TACT.py file, the base_url variable should be changed to the relevant part you are on

## Running the tests

The python script takes 1-2 arguments. You NEED to input the .jar file. You can also optionally provide a test number to start at

Samples:

```
python TACT.py JARFILE.jar 4

python TACT.py JARFILE.jar
```

## Contributing

Feel free to make a pull request/get in contact with me if you have improvements. This code was written up in 2 hours, so I know it's not the best

## Known Problems

TACT doesn't place nice when invalid input is given to the ACT. You could fail a lot of tests because points we're simply put too close together.
