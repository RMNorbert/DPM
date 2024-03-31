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


### Commands to filter examples:

- In case of arguments provided in the configurations: 

```commandline
python filter.py
```

- By providing them in the command line

```commandline
python filter.py --filter-type img  --csv-list example.csv example2.csv --label-list example1 example2
```

| arg          | description |  default value| 
|--------------|-------------|---------------|
| --filter-type| The result of filtering. img - only the image, label - both the image and label related files are generated.| img |
| --output     | The path and the file name where the filtered data will be saved. |   ./image_list |
| --csv-list   | The list of csv files to use for filtering. You can give one or multiple files separated by a space. | None |
| --label-list | The list of labels(or field values) to use for filtering. You can give one or multiple labels separated by a space. | None |

---

### Commands to download examples:
- In case of arguments provided in the configurations: 

```commandline
python download.py
```

- By providing them in the command line

```commandline
python filter.py --filter-type img  --csv-list example.csv example2.csv --label-list example1 example2
```

| arg             | description                                                                             |  default value              | 
|-----------------|-----------------------------------------------------------------------------------------|-----------------------------|
| --image_list    | The filename that contains the split and image IDs of the images to download.           | image_list                  |
| --processes     | The number of parallel processes to use .                                               | 6                           |
| --output_folder | Folder where to download the images.                                                    | None (the current directory)|
| --request       | The download source type. True to use requests, false to use boto3(AWS SDK) to download | True                        |
| --bucket_name   | The name of the S3 bucket where the images are located.                                 | None                        |
