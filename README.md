# MD Notes

<p align="center">
<img src="img/MDNotes.png" alt="drawing" width="200"/>
</p>

A simple script to organize markdown notes written in Python.
## Getting started
- Clone this repo
    ```
    git clone https://github.com/aldipiroli/md_notes
    ```
- In the file `config/config.yaml` change the location of where the notes will be saved
  ```
  DATA_STORAGE:
    BASE_PATH: "data/path"
  ```
- Create a new note using 
    ```
    python new_note.py
    ```
    This will create a default note that looks like this:
    ```md
    #
    date: 16/06/2023 - 16:51:37

    tags: #note 
    #
    ```

## Additional Settings
- You can add tags to a not while creating it using
  ```
  python new_note.py -t tag1,tag2,tag3
  ```
  **Note**: the tags are separate via comma, so that tag1,tag2,tag3 becomes  `tags: #tag1, #tag2, #tag3`.

