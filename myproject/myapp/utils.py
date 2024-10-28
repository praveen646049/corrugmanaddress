import os
import shutil
import time

def backup_database(db_path, backup_dir):
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    backup_file = os.path.join(backup_dir, f'backup_{int(time.time())}.sqlite3')

    try:
        shutil.copy(db_path, backup_file)
        return backup_file
    except Exception as e:
        print(f"Error during backup: {e}")
        return None

# The send_backup_email function is removed since you're not sending emails anymore.
