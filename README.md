# MD Notes
A simple script to organize markdown notes written in Python.

## Getting started
- Clone this repo
    ```
    git clone https://github.com/aldipiroli/md_notes
    ```
- In the file `config/config.yaml` change the location of where the are will be saved
  ```
  DATA_STORAGE:
    BASE_PATH: "data/path"
  ```
- Create a new note using 
    ```
    python new_note.py
    ```
## Additional Settings
- You can add tags to a not while creating it using
  ```
  python new_note.py -t tag1,tag2,tag3
  ```
  **Note**: the tags are separate via comma, so that tag1,tag2,tag3 becomes  `tags: #tag1, #tag2, #tag3`.

