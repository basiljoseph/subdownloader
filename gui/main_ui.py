# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sun Aug  3 18:16:43 2008
#      by: PyQt4 UI code generator 4.4.3-snapshot-20080731
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(835, 726)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/subdownloader.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0, 24, 835, 678))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.vboxlayout = QtGui.QVBoxLayout()

        self.tabs = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy)
        self.tabs.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabs.setObjectName("tabs")
        self.tab = QtGui.QWidget()
        self.tab.setGeometry(QtCore.QRect(0, 0, 811, 629))
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.buttonPlay = QtGui.QPushButton(self.tab)
        self.buttonPlay.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonPlay.sizePolicy().hasHeightForWidth())
        self.buttonPlay.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPlay.setIcon(icon1)
        self.buttonPlay.setObjectName("buttonPlay")
        self.horizontalLayout_4.addWidget(self.buttonPlay)
        self.buttonDownload = QtGui.QPushButton(self.tab)
        self.buttonDownload.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonDownload.sizePolicy().hasHeightForWidth())
        self.buttonDownload.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.buttonDownload.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonDownload.setIcon(icon2)
        self.buttonDownload.setObjectName("buttonDownload")
        self.horizontalLayout_4.addWidget(self.buttonDownload)
        self.buttonIMDB = QtGui.QPushButton(self.tab)
        self.buttonIMDB.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonIMDB.sizePolicy().hasHeightForWidth())
        self.buttonIMDB.setSizePolicy(sizePolicy)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/imdb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonIMDB.setIcon(icon3)
        self.buttonIMDB.setIconSize(QtCore.QSize(32, 16))
        self.buttonIMDB.setObjectName("buttonIMDB")
        self.horizontalLayout_4.addWidget(self.buttonIMDB)
        spacerItem = QtGui.QSpacerItem(275, 13, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.filterLanguageForVideo = QtGui.QComboBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterLanguageForVideo.sizePolicy().hasHeightForWidth())
        self.filterLanguageForVideo.setSizePolicy(sizePolicy)
        self.filterLanguageForVideo.setMinimumSize(QtCore.QSize(100, 0))
        self.filterLanguageForVideo.setObjectName("filterLanguageForVideo")
        self.horizontalLayout_4.addWidget(self.filterLanguageForVideo)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.splitter = QtGui.QSplitter(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setMinimumSize(QtCore.QSize(0, 400))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.groupBox_folderselect = QtGui.QGroupBox(self.splitter)
        self.groupBox_folderselect.setObjectName("groupBox_folderselect")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_folderselect)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.buttonSearchSelectVideos = QtGui.QPushButton(self.groupBox_folderselect)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSearchSelectVideos.sizePolicy().hasHeightForWidth())
        self.buttonSearchSelectVideos.setSizePolicy(sizePolicy)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/open_video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonSearchSelectVideos.setIcon(icon4)
        self.buttonSearchSelectVideos.setIconSize(QtCore.QSize(24, 24))
        self.buttonSearchSelectVideos.setObjectName("buttonSearchSelectVideos")
        self.horizontalLayout_6.addWidget(self.buttonSearchSelectVideos)
        self.buttonSearchSelectFolder = QtGui.QPushButton(self.groupBox_folderselect)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSearchSelectFolder.sizePolicy().hasHeightForWidth())
        self.buttonSearchSelectFolder.setSizePolicy(sizePolicy)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/open_folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonSearchSelectFolder.setIcon(icon5)
        self.buttonSearchSelectFolder.setIconSize(QtCore.QSize(24, 24))
        self.buttonSearchSelectFolder.setObjectName("buttonSearchSelectFolder")
        self.horizontalLayout_6.addWidget(self.buttonSearchSelectFolder)
        spacerItem1 = QtGui.QSpacerItem(88, 31, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.line_4 = QtGui.QFrame(self.groupBox_folderselect)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_3.addWidget(self.line_4)
        self.folderView = QtGui.QTreeView(self.groupBox_folderselect)
        self.folderView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.folderView.setObjectName("folderView")
        self.verticalLayout_3.addWidget(self.folderView)
        self.buttonFind = QtGui.QPushButton(self.groupBox_folderselect)
        self.buttonFind.setEnabled(False)
        self.buttonFind.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.buttonFind.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonFind.setIcon(icon6)
        self.buttonFind.setIconSize(QtCore.QSize(24, 24))
        self.buttonFind.setObjectName("buttonFind")
        self.verticalLayout_3.addWidget(self.buttonFind)
        self.groupBox_videosFound = QtGui.QGroupBox(self.splitter)
        self.groupBox_videosFound.setObjectName("groupBox_videosFound")
        self.hboxlayout = QtGui.QHBoxLayout(self.groupBox_videosFound)

        self.videoView = QtGui.QTreeView(self.groupBox_videosFound)
        self.videoView.setObjectName("videoView")
        self.hboxlayout.addWidget(self.videoView)
        self.verticalLayout_4.addWidget(self.splitter)
        self.tabs.addTab(self.tab, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setGeometry(QtCore.QRect(0, 0, 811, 629))
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.movieNameText = QtGui.QLineEdit(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.movieNameText.sizePolicy().hasHeightForWidth())
        self.movieNameText.setSizePolicy(sizePolicy)
        self.movieNameText.setObjectName("movieNameText")
        self.horizontalLayout.addWidget(self.movieNameText)
        self.buttonSearchByName = QtGui.QPushButton(self.tab_3)
        self.buttonSearchByName.setFlat(False)
        self.buttonSearchByName.setObjectName("buttonSearchByName")
        self.horizontalLayout.addWidget(self.buttonSearchByName)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem2 = QtGui.QSpacerItem(26, 26, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_3 = QtGui.QLabel(self.tab_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.searchSitesCombo = QtGui.QComboBox(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchSitesCombo.sizePolicy().hasHeightForWidth())
        self.searchSitesCombo.setSizePolicy(sizePolicy)
        self.searchSitesCombo.setObjectName("searchSitesCombo")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/sites/opensubtitles.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchSitesCombo.addItem(icon7, QtCore.QString())
        self.horizontalLayout_2.addWidget(self.searchSitesCombo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.buttonDownloadByTitle = QtGui.QPushButton(self.tab_3)
        self.buttonDownloadByTitle.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonDownloadByTitle.sizePolicy().hasHeightForWidth())
        self.buttonDownloadByTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.buttonDownloadByTitle.setFont(font)
        self.buttonDownloadByTitle.setIcon(icon2)
        self.buttonDownloadByTitle.setObjectName("buttonDownloadByTitle")
        self.horizontalLayout_3.addWidget(self.buttonDownloadByTitle)
        self.buttonIMDBByTitle = QtGui.QPushButton(self.tab_3)
        self.buttonIMDBByTitle.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonIMDBByTitle.sizePolicy().hasHeightForWidth())
        self.buttonIMDBByTitle.setSizePolicy(sizePolicy)
        self.buttonIMDBByTitle.setIcon(icon3)
        self.buttonIMDBByTitle.setIconSize(QtCore.QSize(32, 16))
        self.buttonIMDBByTitle.setObjectName("buttonIMDBByTitle")
        self.horizontalLayout_3.addWidget(self.buttonIMDBByTitle)
        spacerItem3 = QtGui.QSpacerItem(328, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.label_10 = QtGui.QLabel(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.filterLanguageForTitle = QtGui.QComboBox(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterLanguageForTitle.sizePolicy().hasHeightForWidth())
        self.filterLanguageForTitle.setSizePolicy(sizePolicy)
        self.filterLanguageForTitle.setMinimumSize(QtCore.QSize(100, 0))
        self.filterLanguageForTitle.setObjectName("filterLanguageForTitle")
        self.horizontalLayout_3.addWidget(self.filterLanguageForTitle)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.groupBox_4 = QtGui.QGroupBox(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName("groupBox_4")
        self.hboxlayout1 = QtGui.QHBoxLayout(self.groupBox_4)
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.moviesView = QtGui.QTreeView(self.groupBox_4)
        self.moviesView.setObjectName("moviesView")
        self.hboxlayout1.addWidget(self.moviesView)
        self.vboxlayout1.addWidget(self.groupBox_4)
        self.verticalLayout_2.addLayout(self.vboxlayout1)
        self.tabs.addTab(self.tab_3, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setGeometry(QtCore.QRect(0, 0, 811, 629))
        self.tab_4.setObjectName("tab_4")
        self.vboxlayout2 = QtGui.QVBoxLayout(self.tab_4)
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.vboxlayout3 = QtGui.QVBoxLayout()
        self.vboxlayout3.setObjectName("vboxlayout3")
        self.groupBox_2 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.buttonUploadBrowseFolder = QtGui.QToolButton(self.groupBox_2)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/openfolder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUploadBrowseFolder.setIcon(icon8)
        self.buttonUploadBrowseFolder.setIconSize(QtCore.QSize(24, 24))
        self.buttonUploadBrowseFolder.setObjectName("buttonUploadBrowseFolder")
        self.horizontalLayout_5.addWidget(self.buttonUploadBrowseFolder)
        self.line_3 = QtGui.QFrame(self.groupBox_2)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_5.addWidget(self.line_3)
        self.buttonUploadPlusRow = QtGui.QToolButton(self.groupBox_2)
        self.buttonUploadPlusRow.setEnabled(True)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUploadPlusRow.setIcon(icon9)
        self.buttonUploadPlusRow.setIconSize(QtCore.QSize(24, 24))
        self.buttonUploadPlusRow.setObjectName("buttonUploadPlusRow")
        self.horizontalLayout_5.addWidget(self.buttonUploadPlusRow)
        self.buttonUploadMinusRow = QtGui.QToolButton(self.groupBox_2)
        self.buttonUploadMinusRow.setEnabled(False)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUploadMinusRow.setIcon(icon10)
        self.buttonUploadMinusRow.setIconSize(QtCore.QSize(24, 24))
        self.buttonUploadMinusRow.setObjectName("buttonUploadMinusRow")
        self.horizontalLayout_5.addWidget(self.buttonUploadMinusRow)
        self.buttonUploadDeleteAllRow = QtGui.QToolButton(self.groupBox_2)
        self.buttonUploadDeleteAllRow.setEnabled(True)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/delete_all.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUploadDeleteAllRow.setIcon(icon11)
        self.buttonUploadDeleteAllRow.setIconSize(QtCore.QSize(24, 24))
        self.buttonUploadDeleteAllRow.setObjectName("buttonUploadDeleteAllRow")
        self.horizontalLayout_5.addWidget(self.buttonUploadDeleteAllRow)
        self.line_2 = QtGui.QFrame(self.groupBox_2)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_5.addWidget(self.line_2)
        self.buttonUploadUpRow = QtGui.QToolButton(self.groupBox_2)
        self.buttonUploadUpRow.setEnabled(False)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/images/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUploadUpRow.setIcon(icon12)
        self.buttonUploadUpRow.setIconSize(QtCore.QSize(24, 24))
        self.buttonUploadUpRow.setObjectName("buttonUploadUpRow")
        self.horizontalLayout_5.addWidget(self.buttonUploadUpRow)
        self.buttonUploadDownRow = QtGui.QToolButton(self.groupBox_2)
        self.buttonUploadDownRow.setEnabled(False)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/images/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUploadDownRow.setIcon(icon13)
        self.buttonUploadDownRow.setIconSize(QtCore.QSize(24, 24))
        self.buttonUploadDownRow.setObjectName("buttonUploadDownRow")
        self.horizontalLayout_5.addWidget(self.buttonUploadDownRow)
        spacerItem4 = QtGui.QSpacerItem(401, 33, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.buttonUpload = QtGui.QPushButton(self.groupBox_2)
        self.buttonUpload.setEnabled(True)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.buttonUpload.setFont(font)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/images/upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonUpload.setIcon(icon14)
        self.buttonUpload.setObjectName("buttonUpload")
        self.horizontalLayout_5.addWidget(self.buttonUpload)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.uploadView = UploadListView(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uploadView.sizePolicy().hasHeightForWidth())
        self.uploadView.setSizePolicy(sizePolicy)
        self.uploadView.setAcceptDrops(True)
        self.uploadView.setDragEnabled(True)
        self.uploadView.setDragDropMode(QtGui.QAbstractItemView.DropOnly)
        self.uploadView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.uploadView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.uploadView.setGridStyle(QtCore.Qt.DotLine)
        self.uploadView.setObjectName("uploadView")
        self.verticalLayout.addWidget(self.uploadView)
        self.line = QtGui.QFrame(self.groupBox_2)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.vboxlayout3.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.gridlayout = QtGui.QGridLayout(self.groupBox)
        self.gridlayout.setObjectName("gridlayout")
        self.label_4 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(10, 16777215))
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 0, 1, 1, 1)
        self.uploadIMDB = QtGui.QComboBox(self.groupBox)
        self.uploadIMDB.setObjectName("uploadIMDB")
        self.uploadIMDB.addItem(QtCore.QString())
        self.gridlayout.addWidget(self.uploadIMDB, 0, 2, 1, 1)
        self.buttonUploadFindIMDB = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonUploadFindIMDB.sizePolicy().hasHeightForWidth())
        self.buttonUploadFindIMDB.setSizePolicy(sizePolicy)
        self.buttonUploadFindIMDB.setMinimumSize(QtCore.QSize(0, 0))
        self.buttonUploadFindIMDB.setMaximumSize(QtCore.QSize(50, 16777215))
        self.buttonUploadFindIMDB.setIcon(icon6)
        self.buttonUploadFindIMDB.setObjectName("buttonUploadFindIMDB")
        self.gridlayout.addWidget(self.buttonUploadFindIMDB, 0, 3, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QtCore.QSize(10, 16777215))
        self.label_8.setObjectName("label_8")
        self.gridlayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridlayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.uploadLanguages = QtGui.QComboBox(self.groupBox)
        self.uploadLanguages.setObjectName("uploadLanguages")
        self.gridlayout.addWidget(self.uploadLanguages, 1, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridlayout.addWidget(self.label_6, 2, 1, 1, 1)
        self.uploadReleaseText = QtGui.QLineEdit(self.groupBox)
        self.uploadReleaseText.setObjectName("uploadReleaseText")
        self.gridlayout.addWidget(self.uploadReleaseText, 2, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridlayout.addWidget(self.label_7, 3, 1, 1, 1)
        self.uploadComments = QtGui.QTextEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uploadComments.sizePolicy().hasHeightForWidth())
        self.uploadComments.setSizePolicy(sizePolicy)
        self.uploadComments.setMaximumSize(QtCore.QSize(16777215, 100))
        self.uploadComments.setObjectName("uploadComments")
        self.gridlayout.addWidget(self.uploadComments, 3, 2, 1, 1)
        self.vboxlayout3.addWidget(self.groupBox)
        self.vboxlayout2.addLayout(self.vboxlayout3)
        self.tabs.addTab(self.tab_4, "")
        self.vboxlayout.addWidget(self.tabs)
        self.verticalLayout_5.addLayout(self.vboxlayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setGeometry(QtCore.QRect(0, 702, 835, 24))
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 835, 24))
        self.menuBar.setObjectName("menuBar")
        self.menuMain = QtGui.QMenu(self.menuBar)
        self.menuMain.setObjectName("menuMain")
        self.menu_Help = QtGui.QMenu(self.menuBar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menuBar)
        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.action_HelpHomepage = QtGui.QAction(MainWindow)
        self.action_HelpHomepage.setObjectName("action_HelpHomepage")
        self.action_HelpAbout = QtGui.QAction(MainWindow)
        self.action_HelpAbout.setObjectName("action_HelpAbout")
        self.action_HelpBug = QtGui.QAction(MainWindow)
        self.action_HelpBug.setObjectName("action_HelpBug")
        self.action_HelpDonation = QtGui.QAction(MainWindow)
        self.action_HelpDonation.setObjectName("action_HelpDonation")
        self.action_ShowPreferences = QtGui.QAction(MainWindow)
        self.action_ShowPreferences.setObjectName("action_ShowPreferences")
        self.menuMain.addAction(self.action_ShowPreferences)
        self.menuMain.addSeparator()
        self.menuMain.addAction(self.action_Quit)
        self.menu_Help.addAction(self.action_HelpHomepage)
        self.menu_Help.addAction(self.action_HelpDonation)
        self.menu_Help.addAction(self.action_HelpBug)
        self.menu_Help.addSeparator()
        self.menu_Help.addAction(self.action_HelpAbout)
        self.menuBar.addAction(self.menuMain.menuAction())
        self.menuBar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "SubDownloader", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonPlay.setText(QtGui.QApplication.translate("MainWindow", "Play", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonDownload.setText(QtGui.QApplication.translate("MainWindow", "Download", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonIMDB.setText(QtGui.QApplication.translate("MainWindow", "Movie Info", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Filter by :", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_folderselect.setTitle(QtGui.QApplication.translate("MainWindow", "Select the video/folder that needs subtitles:", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSearchSelectVideos.setToolTip(QtGui.QApplication.translate("MainWindow", "Select videos that need subtitles", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSearchSelectVideos.setText(QtGui.QApplication.translate("MainWindow", "Select videos...", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSearchSelectFolder.setToolTip(QtGui.QApplication.translate("MainWindow", "Click here to Search the subtitles of the movies in that folder", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSearchSelectFolder.setText(QtGui.QApplication.translate("MainWindow", "Select folder...  ", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonFind.setToolTip(QtGui.QApplication.translate("MainWindow", "Click here to Search the subtitles of the movies in that folder", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonFind.setText(QtGui.QApplication.translate("MainWindow", "Search subtitles", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_videosFound.setTitle(QtGui.QApplication.translate("MainWindow", "Videos/Subtitles found:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Search from Video file(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSearchByName.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Site:", None, QtGui.QApplication.UnicodeUTF8))
        self.searchSitesCombo.setItemText(0, QtGui.QApplication.translate("MainWindow", "OpenSubtitles.org", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonDownloadByTitle.setText(QtGui.QApplication.translate("MainWindow", "Download", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonIMDBByTitle.setText(QtGui.QApplication.translate("MainWindow", "Movie Info", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Filter by :", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Subtitles found:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Search by Movie Name", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Select Folder with Videos / Subtitles: ", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonUploadBrowseFolder.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonUploadPlusRow.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonUploadMinusRow.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonUploadDeleteAllRow.setToolTip(QtGui.QApplication.translate("MainWindow", "Empty the list", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonUploadDeleteAllRow.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonUploadUpRow.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonUploadDownRow.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonUpload.setText(QtGui.QApplication.translate("MainWindow", "Upload", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Details", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff0000;\">*</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "IMDB: ", None, QtGui.QApplication.UnicodeUTF8))
        self.uploadIMDB.setItemText(0, QtGui.QApplication.translate("MainWindow", "Click on FIND button to choose the IMDB link", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonUploadFindIMDB.setText(QtGui.QApplication.translate("MainWindow", "Find", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff0000;\">*</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Language:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Release:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Comments:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "Upload subtitles", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMain.setTitle(QtGui.QApplication.translate("MainWindow", "&Main", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_HelpHomepage.setText(QtGui.QApplication.translate("MainWindow", "Visit our &Site", None, QtGui.QApplication.UnicodeUTF8))
        self.action_HelpAbout.setText(QtGui.QApplication.translate("MainWindow", "&About Subdownloader", None, QtGui.QApplication.UnicodeUTF8))
        self.action_HelpBug.setText(QtGui.QApplication.translate("MainWindow", "I found a &bug/error", None, QtGui.QApplication.UnicodeUTF8))
        self.action_HelpDonation.setText(QtGui.QApplication.translate("MainWindow", "Make a &Donation", None, QtGui.QApplication.UnicodeUTF8))
        self.action_ShowPreferences.setText(QtGui.QApplication.translate("MainWindow", "&Preferences", None, QtGui.QApplication.UnicodeUTF8))

from uploadlistview import UploadListView
import images_rc
