import widget

class Container(widget.Widget):
    """
    Base container widget - this widget holds and layouts the widgets
    added to it. All layouts and containers should inherit from this class.
    """
    def __init__(self):
        """
        Constructor.
        """
        widget.Widget.__init__(self)
        self._widgets = []

    def add(self, widget):
        """
        Add a widget to the container.
        """
        self._widgets.append(widget)
        widget._parent = self
        self.layout()
    
    def layout(self):
        """
        Layout the widgets in the container
        """
        pass
    
    def paint(self, surface):
        """
        Paint all widgets in the container. Classes overloading this method
        should either draw its widgets or call this function.
        """
        for widget in reversed(self._widgets):
            widget.paint(surface)
    
    def get_widget_at(self, point):
        """
        Returns the widget at the given position. This usually traverses down
        with a breadth first search until the given element is found.
        """
        for widget in self._widgets:
            result = widget.get_widget_at(point)
            if result != None:
                return result
        return None
