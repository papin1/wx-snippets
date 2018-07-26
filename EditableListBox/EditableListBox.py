import wx
import wx.gizmos as gizmos

class MainPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        # create control
        self.ebox = gizmos.EditableListBox(self, -1, 'title')
        # bind right-click
        self.ebox.Bind(wx.EVT_CONTEXT_MENU, self.onEditableListBoxContextMenu)

    def onEditableListBoxContextMenu(self, evt):
        # On right-click the underlying ListCtrl ListItem always gets the focus
        # even if it's not the current selected item
        # So, this is the way to get the index of the right-clicked item
        idx = self.ebox.GetListCtrl().GetFocusedItem()  # similar to evt.GetIndex()
        # And to get the value (as a string):
        string = self.ebox.GetStrings()[idx]
