# Create csv file from Drachenwald recommendation emails

## What does it do?
This little Python script takes a bunch of recommendation mails saved in a local directory and extracts the machine readable part of the email and writes it into a CSW (comma separated value) format. The seperator is in fact not a comma but the | symbol so you will have to selecg that when you import it into Calc or Excel.

## What you need.
 - Python 3 installation
 - Preferrably Linux but there is no reason why it shouldn't work on Windows or MacOS. You mihgt need to change the first line to point to your local python installation though.

## How it works.

 - Copy the files into a directory on your machine (or checkout the repo from git if you prefer).
 - Save the emails as .eml files into the recommendations directory.
 - Run the script recommendations.py. it will try to read email files form the directory recommendations in the local directory and write the output to recommendations.csv.
 - If you store the emails somewhere else you can give input directory and output directory as command line options like below.

```shell
   ./recommendations.py ../../some_input_dir  /tmp/out.csv
```

## Doesn't work? Need help?

If you got trouble to make it work feel free to leave a comment in Github or find Vitus Polonius on FB.