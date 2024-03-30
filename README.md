# DPM
[Table of content:](#description)
- [Used Technologies](#used-technologies)
- [Details](#details)
- [Commands](#to-run)

**DPM is an extremely useful data preparation tool initially developed for personal use, yet its functionalities extend to benefit for example: data scientists, machine learning enthusiasts, and anyone interested in efficient data handling.**

---
## Used Technologies:
- Python (3.10.12)
- PyYAML (6.0.1)
- boto3 (1.34.74)
- botocore (1.34.74)
- requests (2.31.0)
- tqdm (4.66.2)
- autopep8 (2.0.4)

---
## Details

- Download
  - Works when the file is publicly available. 
  - Currently configured to download from:
    - Amazon S3 bucket
    - Google Drive

- Filter
  - Filter the dataset according to specific labels (or field values), and extract label-related(field related) data based on specific field values.
    - Currently filtering support csv files for source

---
## To run
1. Navigate into the Preparator directory </br></br>
2. Create virtual environment & activate </br></br>
3. Install the requirements </br></br>

```commandline
 pip install -r requirements.txt
```
Arguments can be set in the configurations or by providing them in the command line

### Commands to filter examples:

```commandline
python filter.py
```



```commandline
python filter.py --filter-type img  --csv-list example.csv example2.csv --label-list example1 example2
```
The ```--output``` (optional, default is the current directory)

| arg          | description |
|--------------|-------------|
| --filter-type|             |
| --output     |             |
| --csv-list   |             |
| --label-list |             |

---

### Commands to download examples:

```commandline
python download.py
```

