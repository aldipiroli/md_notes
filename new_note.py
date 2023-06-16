import os
import argparse
from datetime import datetime
import yaml


def read_config(config_path):
    with open(config_path, "r") as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return config

def create_new_note_folder(config, args):
    DATA_PATH = config["DATA_STORAGE"]["BASE_PATH"]
    assert os.path.isdir(DATA_PATH)

    date = datetime.today().strftime("%Y_%m_%d")
    note_path_dir = os.path.join(DATA_PATH, date)
    if not os.path.exists(note_path_dir):
        os.makedirs(note_path_dir)

    filenames = next(os.walk(note_path_dir), (None, None, []))[2]

    # ----- note name -----
    note_name = config["DATA_STORAGE"]["BASE_NOTE_NAME"]
    if config["DATA_STORAGE"]["USE_NOTE_ID"]:
        note_id = str(len(filenames)).zfill(2)
        note_name += "_%s" % (note_id)
    note_path_file = os.path.join(note_path_dir, "%s.md" % note_name)

    template_text = get_template_infos(config, args)
    create_note_template(note_path_file, template_text)

def get_template_infos(config, args):
    BLOCK_LINE = "#"
    template_text = ""

    tags = args.tags.split(",") if args.tags is not None else []

    creation_time = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
    creation_time_str = "date: %s" % (creation_time)

    tags_str = "tags: "
    for t in tags:
        tags_str += "#%s " % (t)

    template_text += "%s\n" % (BLOCK_LINE)
    template_text += "%s\n\n" % (creation_time_str)
    template_text += "%s\n" % (tags_str)
    template_text += "%s\n" % (BLOCK_LINE)

    return template_text


def create_note_template(note_path_file, template_text):
    if os.path.isfile(note_path_file):
        print("Note already exists: %s" % note_path_file)
    else:
        f = open(note_path_file, "w")
        f.write(template_text)
        f.close()
        print("Created note: %s" % (note_path_file))



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n",
        "--new",
        action="store_true",
        default=False,
        help="Creates new file even if a note of the same day already exists",
    )
    parser.add_argument("-t", "--tags", type=str, help="")
    args = parser.parse_args()

    config = read_config(config_path="config/config.yaml")
    create_new_note_folder(config=config, args=args)


if __name__ == "__main__":
    main()
