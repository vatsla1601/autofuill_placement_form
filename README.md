# Autofill Placement Form Automation

Automate the manual procedure of filling Google Forms for placements using Selenium and Chrome Driver.

## Prerequisites

1. Download [Chrome Driver](https://sites.google.com/chromium.org/driver/) compatible with your Chrome Browser version. Check your Chrome Browser version by clicking on the three dots -> Help -> About Google Chrome.

   [Tutorial Video on Downloading Chrome Driver](https://youtu.be/KqWUC-xWYpA?si=oOxZBqGgA9sMxGrI)

2. Install Selenium:

   ```bash/ terminal
   pip install selenium

## Configuration

Edit the parameters in the script according to your use:


data_tuple = (
    ("20BCS5064", "Vatsla", "CSE", "Res", "vats@", "9999"),
    ("20BCS0000", "Trish", "CSE", "Res", "trish@", "999")
)


## Usage

Update the XPath according to the Google Form:

Right-click on the box where you fill the form, for example, UID and then there is a box to fill your UID in. 
Inspect -> Right-click highlighted HTML -> Copy -> Copy XPath.

Run the script:
python autofill_placement_form.py

Reference google form used:
https://docs.google.com/forms/d/e/1FAIpQLSdrfsACGIRNG33kxgq9a6bmdslqne3HPkGNGIW84S3XET7uUg/viewform?usp=sf_link

## Output 

https://www.loom.com/share/66a0f0ad46e4441197a68
45ed7ff8f00?sid=1fe93178-3a26-4854-9caf-a7e7169d0
20b

## Contribution
Feel free to contribute by opening issues or creating pull requests.
