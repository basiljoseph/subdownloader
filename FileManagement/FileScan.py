#!/usr/bin/env python
# -*- coding: utf-8 -*-

##    Copyright (C) 2007 Ivan Garcia  capiscuas@gmail.com
##    This program is free software; you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation; either version 2 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License along
##    with this program; if not, write to the Free Software Foundation, Inc.,
##    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


import os.path
import logging
from FileManagement import get_extension
import RecursiveParser
import modules.videofile as videofile
import modules.subtitlefile as subtitlefile
import modules.metadata as metadata

log = logging.getLogger("subdownloader.FileManagement.FileScan")

def FakeProgress(count,msg=""):
    pass

def ScanFilesFolders(filepaths,recursively = True,report_progress=None, progress_end=None):
    all_videos_found = []
    all_subs_found = []
    for path in filepaths:
        log.debug("Scanning: %s"% path)
        if os.path.isdir(path):
            videos_found, subs_found = ScanFolder(path,recursively = True,report_progress=report_progress, progress_end=progress_end)
            all_videos_found += videos_found
            all_subs_found += subs_found
        else:
            if get_extension(path).lower() in videofile.VIDEOS_EXT:
                all_videos_found.append(videofile.VideoFile(path))
            tmp_videos, subs_found = ScanFolder(os.path.dirname(path),recursively = False,report_progress=report_progress, progress_end=progress_end) 
            all_subs_found += subs_found #Interested to know which subtitles we have in the same folder
    return all_videos_found, all_subs_found

"""Scanning all the Video and Subtitle files inside a Folder/Recursive Folders"""
def ScanFolder(folderpath,recursively = True,report_progress=None, progress_end=None):
    #Let's reset the progress bar to 0%
    log.debug("Scanning Folder %s" % folderpath)
    
    if report_progress == None:
        report_progress = FakeProgress
    
    #Let's reset the progress bar to 0%
    print 
    report_progress(0)

    parser = RecursiveParser.RecursiveParser()
    files_found = []
    try:
        # it's a file
        open(folderpath, 'r')
        if get_extension(folderpath).lower() in videofile.VIDEOS_EXT:
            files_found.append(folderpath)
        folderpath = os.path.dirname(folderpath)
    except IOError:
        # it's a directory
        #Scanning VIDEOS
        files_found = parser.getRecursiveFileList(folderpath, videofile.VIDEOS_EXT)
        
    videos_found = []
    # only work the video files if any were found
    if len(files_found):
        percentage = 100 / len(files_found)
        count = 0
        for i, filepath in enumerate(files_found):
            log.debug("Parsing %s ..."% filepath)
            if metadata.parse(filepath):
                videos_found.append(videofile.VideoFile(filepath))
            count += percentage

            if not report_progress(): #If it has been canceled
                return [], []
            report_progress(count,"Parsing video: %s"% os.path.basename(filepath))
    report_progress(0)
    
    #Scanning Subs
    files_found = parser.getRecursiveFileList(folderpath,subtitlefile.SUBTITLES_EXT)
    subs_found = []
    # only work the subtitles if any were found
    if len(files_found):
        percentage = 100 / len(files_found)
        count = 0
        for i, filepath in enumerate(files_found):
            subs_found.append(subtitlefile.SubtitleFile(online = False,id = filepath))
            count += percentage
            report_progress(count,"Parsing sub: " + os.path.basename(filepath))
    report_progress(100,"Finished hashing")
    if progress_end:
        progress_end()
        
    return videos_found,subs_found
    


