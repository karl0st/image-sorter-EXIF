# image-sorter-EXIF

### Requirements

1. Install [pip](https://pip.pypa.io/en/stable/installation/)
2. Run `pip install -r requirements.txt`

### Usage

You need to comment/uncomment each step manually e.g. for renaming: <br>
```py
rename_image(file)
# sort_images_year(file)
# sort_images_month(file)
```

### Result
```
Folder/
├─ yyyy/
│  ├─ mm/
│  │  ├─ yy-mm-dd hh-nn-ss
│  ├─ mm/
│  │  ├─ yy-mm-dd hh-nn-ss
│  ├─ mm/
│  │  ├─ yy-mm-dd hh-nn-ss
```

yy-mm-dd hh-nn-ss <br>
`22-05-29 22:22:22`
