#!/usr/bin/env python
# coding:utf-8

import os
import sys
import time

from optparse import OptionParser

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import gntp.notifier

class EventHandler(FileSystemEventHandler):

    def __init__(self, command, detector):
        self.command = command
        self.detector = detector
        super(FileSystemEventHandler)

    def on_created(self, event):
        if event.is_directory:
            print 'directory \'{0}\' created.'.format(event.src_path)
        else:
            print 'file \'{0}\' created.'.format(event.src_path)
            if self.detector in event.src_path:
                print 'executing', self.command, '...'
                os.system(self.command)
                gntp.notifier.mini('watch.py: command executed.')

    def on_modified(self, event):
        if event.is_directory:
            print 'directory \'{0}\' modified.'.format(event.src_path)
        else:
            print 'file \'{0}\' modified.'.format(event.src_path)
            if self.detector in event.src_path:
                print 'executing', self.command, '...'
                os.system(self.command)
                gntp.notifier.mini('watch.py: command executed.')

    def on_deleted(self, event):
        if event.is_directory:
            print 'directory \'{0}\' deleted.'.format(event.src_path)
        else:
            print 'file \'{0}\' deleted.'.format(event.src_path)

def main():

    parser = OptionParser()
    parser.add_option('-c', '--cmd', dest='command', default='make',
                      help='command that executed by this program')
    parser.add_option('-d', '--detector', dest='detector', default='.tex',
                      help='extention that you wanna keep watch')

    (options, args) = parser.parse_args()

    print 'make observer...'

    watch_dir = args[0]
    command   = options.command
    detector  = options.detector

    print 'watch directory:', watch_dir
    print 'exec command:', command
    print 'detector:', detector

    event_handler = EventHandler(command, detector)
    observer = Observer()
    observer.schedule(event_handler, watch_dir)
    observer.start()
    print 'observer start!!'

    try:
        while True:
            time.sleep(10)
    except (Exception, KeyboardInterrupt):
        observer.stop()
        print 'observer canceled'
    observer.join()
    print 'observer finished!!'

if __name__ == '__main__':
    main()

