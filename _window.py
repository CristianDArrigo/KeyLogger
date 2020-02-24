import wx
import keyboard as kb


class _frame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(_frame, self).__init__(*args, **kwargs)
        self.basicGUI()
        self.text = ''

    def basicGUI(self):
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()
        exitItem = fileButton.Append(wx.ID_EXIT, 'Exit', 'Exit the program...')
        menuBar.Append(fileButton, 'File')
        keyLoggerButton = wx.Menu()
        recordItem = keyLoggerButton.Append(wx.ID_ANY, 'Record', 'Start the KeyLogger...')
        writeRecordedItem = keyLoggerButton.Append(wx.ID_ANY, 'Write Recorded', 'Write on the panel the registered '
                                                                                'text...')
        menuBar.Append(keyLoggerButton, 'Record/Write')
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)
        self.Bind(wx.EVT_MENU, self.Record, recordItem)
        self.Bind(wx.EVT_MENU, self.Write, writeRecordedItem)

        panel = wx.Panel(self)
        wx.TextCtrl(panel, pos=(10, 10), size=(250, 150))

        self.SetTitle('KeyLogger')
        self.Show(True)

    def Quit(self, e):
        yesNoBox = wx.MessageDialog(None, 'Do you really want to Exit?..', 'Exit?', wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        if yesNoAnswer == wx.ID_YES:
            self.Close()

    def Record(self, e):
        self.text = kb.record(until='S + F12')

    def Write(self, e):
        if self.text != '':
            kb.play(self.text, speed_factor=100)
        else:
            wx.MessageBox('No text was registered...', 'Info', wx.OK_DEFAULT)
