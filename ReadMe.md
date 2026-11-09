# <center> Hackathon Submission Processor </center>
This python script was made to process projects submitted through <b>DevPost</b> and/or <b>MLH</b> for hackathons. Drop the `.py` file into the same folder as the exported data from the sites and run.

It processes the `.csv` file exported from the submission page and writes the data to another `.csv` file as a `TRUE/FALSE` table for each track the project team has opted into. Verification for teams to meet the requirements for tracks is handled by Hackathon Staff.

Exported data is written as follows:

| Project | Submitter | Source | Track #1 | Track #2 | Track #3 |
| ------- | --------- | ------ | :---: | :---: | :---: |
| Project1 | John Doe | github repo | TRUE | | TRUE |
| Project2 | Jane Doe | github repo |  | |  |
| Project1 | Jack Doe | github repo | TRUE | TRUE | TRUE |

`python` is the only dependency.

Execution of the script is as follows:

```
Enter DevPost CSV Filename:
Press Enter if None.
[ DEVPOST.CSV ] [ ENTER ]

DevPost CSV processed and written to: "devpostProcessed.csv"

Enter MLH CSV Filename
Press Enter if None.
[ DEVPOST.CSV ] [ ENTER ]

MLH CSV processed and written to: "mlhProcessed.csv"
```