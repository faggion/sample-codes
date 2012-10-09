import time,logging,subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ChangeHandler(FileSystemEventHandler):
    def sync(self, event):
        if event.is_directory:
            return
        else:
            subprocess.call('make')
    def on_created(self, event):
        self.sync(event)
    def on_deleted(self, event):
        self.sync(event)
    def on_modified(self, event):
        self.sync(event)

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
